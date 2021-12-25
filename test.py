from unittest import TestCase

from demo import add


class TestOne(TestCase):
    def test_add(self):
        rv = add(1, 1)
        self.assertEqual(rv, 2)

    def test_nonsense(self):
        pass

