import unittest
from utils.path_normalizer import path_normalizer

class TestPathNormalizer(unittest.TestCase):
    def test_path_normalizer(self):
        # Test with a relative path
        self.assertEqual(path_normalizer('folder/../folder/file.txt'), 'folder/file.txt')

        # Test with an absolute path
        self.assertEqual(path_normalizer('/folder/../folder/file.txt'), '/folder/file.txt')

        # Test with an empty path
        self.assertEqual(path_normalizer(''), None)

        # Test with a None path
        self.assertEqual(path_normalizer(None), None)

if __name__ == '__main__':
    unittest.main()