import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for the 'name_function.py."""

    def test_first_last_name(self):
        """Do names like christian bailey work?"""
        formatted_name = get_formatted_name('christian', 'bailey')
        self.assertEqual(formatted_name, 'Christian Bailey')
    
    def test_first_last_middle_name(self):
        """Do names like christian lawrence bailey work?"""
        formatted_name = get_formatted_name(
            'christian', 'bailey', 'lawrence'
        )
        self.assertEqual(formatted_name, 'Christian Lawrence Bailey')

if __name__ == '__main__':
    unittest.main()