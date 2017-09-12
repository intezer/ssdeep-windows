from os.path import join
from os.path import split
from unittest import TestCase

from pip._vendor import six

import ssdeep

_resources_path = join(split(__file__)[0], 'resources')


class TestHash(TestCase):
    def test_hash_file(self):
        # Arrange
        expected_hash =\
            '3:Wttkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkl:Ybkjbkjbkjbkjbkjbkjbkjbkjbkji'
        file1_path = join(_resources_path, 'file_1.txt')

        # Act
        with open(file1_path, 'rb') as file1:
            file1_bytes = file1.read()

        hash_result = ssdeep.hash(file1_bytes)

        # Assert
        self.assertTrue(isinstance(hash_result, (str, six.text_type)))
        self.assertEqual(
            hash_result,
            expected_hash)

    def test_hash_string(self):
        # Arrange
        expected_hash = '3:Hn:Hn'

        # Act
        hash_result = ssdeep.hash('test')

        # Assert
        self.assertTrue(isinstance(hash_result, (str, six.text_type)))
        self.assertEqual(hash_result, expected_hash)

    def test_hash_string_unicode(self):
        # Arrange
        expected_hash = '3:Hn:Hn'

        # Act
        hash_result = ssdeep.hash(u'test')

        # Assert
        self.assertTrue(isinstance(hash_result, six.text_type))
        self.assertEqual(hash_result, expected_hash)


class TestHashFromFile(TestCase):
    def test_hash_file_path(self):
        # Arrange
        expected_hash =\
            '3:Wttkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkl:Ybkjbkjbkjbkjbkjbkjbkjbkjbkji'
        file1_path = join(_resources_path, 'file_1.txt')

        # Act
        hash_result = ssdeep.hash_from_file(file1_path)

        # Assert
        self.assertTrue(isinstance(hash_result, (str, six.text_type)))
        self.assertEqual(
            hash_result,
            expected_hash)


class TestCompare(TestCase):
    def test_two_similar_signatures(self):
        # Arrange
        signature = '3:Wttkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkl:Ybkjbkjbkjbkjbkjbkjbkjbkjbkji'

        # Act
        compare_result = ssdeep.compare(signature, signature)

        # Assert
        self.assertTrue(isinstance(compare_result, int))
        self.assertEqual(compare_result, 100)

    def test_two_different_signatures(self):
        # Arrange
        signature1 = '3:Wttkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkl:Ybkjbkjbkjbkjbkjbkjbkjbkjbkji'
        signature2 = '3:Hn:Hn'

        # Act
        compare_result = ssdeep.compare(signature1, signature2)

        # Assert
        self.assertTrue(isinstance(compare_result, int))
        self.assertEqual(compare_result, 0)
