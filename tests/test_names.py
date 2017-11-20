import unittest

from exactitude import names


class NamesTest(unittest.TestCase):

    def test_parse(self):
        self.assertEqual(names.clean('Hans Well'), 'Hans Well')
        self.assertEqual(names.clean('Hans   Well '), 'Hans Well')
        self.assertEqual(names.clean('"Hans Well"'), 'Hans Well')

    def test_normalize(self):
        self.assertEqual(names.normalize('FOO'), ['FOO'])
        self.assertEqual(names.normalize('xx '), ['xx'])
        self.assertEqual(names.normalize(' '), [])

    def test_domain_validity(self):
        self.assertTrue(names.validate('huhu'))
        self.assertFalse(names.validate(''))
