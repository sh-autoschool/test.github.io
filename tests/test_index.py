import re
import unittest
from pathlib import Path


class IndexHtmlTests(unittest.TestCase):
    def setUp(self):
        self.html = Path('index.html').read_text(encoding='utf-8')

    def test_document_has_expected_app_structure(self):
        self.assertIn('<!doctype html>', self.html.lower())
        self.assertIn('<div id="app">', self.html)
        self.assertIn('id="home"', self.html)
        self.assertIn('id="list"', self.html)
        self.assertIn('id="quiz"', self.html)
        self.assertIn('id="result"', self.html)

    def test_questions_data_exists_and_has_content(self):
        match = re.search(r'const\s+QUESTIONS\s*=\s*(\[[\s\S]*?\])\s*;\s*let\s+state', self.html)
        self.assertIsNotNone(match, 'QUESTIONS array is missing from index.html')
        questions_block = match.group(1)
        self.assertIn('"question"', questions_block)
        self.assertIn('"options"', questions_block)
        self.assertIn('"answer"', questions_block)
        self.assertGreater(questions_block.count('"id":'), 0)

    def test_quiz_logic_is_present(self):
        self.assertIn('function startTest', self.html)
        self.assertIn('function renderQ', self.html)
        self.assertIn('function finish', self.html)
        self.assertIn('function showList', self.html)


if __name__ == '__main__':
    unittest.main()
