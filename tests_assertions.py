from sets import Set
from unittest import TestCase


import unittest


class CruiseFilterTest(TestCase):
    def test_a(self):
        a = 1
        b = 2
        self.assertEqual(a, b)

    def test_b(self):
        a = []
        with self.assertRaises(IndexError, callableObj=a.append(1)) as cm:
            print a[3]
        the_exception = cm.exception
        print a
        self.assertEqual(the_exception.message, 'list index out of range1')

    def test_c(self):
        a = 1.12345
        b = 1.12346
        self.assertAlmostEqual(a, b, places=5)

    def test_d(self):
        a = 1.12345
        b = 1.12346
        self.assertAlmostEqual(a, b, delta=0.000001)

    def test_e(self):
        a = (1, 2)
        b = [1, 3]
        self.assertSequenceEqual(a, b)

    def test_f(self):
        a = [1, 2]
        b = [1, 3]
        self.assertListEqual(a, b)

    def test_g(self):
        a = Set(['John', 'Jane', 'Jack', 'Janice'])
        b = Set(['John', 'Jane', 'Jack', ])
        self.assertSetEqual(a, b)

    def test_h(self):
        a =(1, 2)
        b = (1, 3)
        self.assertTupleEqual(a, b)

    def test_i(self):
        a = {'a': 1, 'b': 2}
        b = {'a': 1, 'b': 3}
        self.assertDictEqual(a, b)

    def test_j(self):
        a = 'a'
        b = 'sjofsj'
        self.assertIn(a, b)

    def test_k(self):
        a = 'a'
        b = 'asjofsj'
        self.assertNotIn(a, b)

    def test_l(self):
        a = 2 + 2
        b = 2 * 2
        self.assertIsNot(a, b)

    def test_m(self):
        a = 2 + 1
        b = 2 * 1
        self.assertIs(a, b)

    def test_n(self):
        a = {'a': 1, 'b': 2, 'c': 3}
        b = {'b': 1, 'a': 2, 'd': 3}
        self.assertDictContainsSubset(b, a)

    def test_o(self):
        a = [0, 0, 1]
        b = [0, 1, 1]
        self.assertItemsEqual(b, a)

    def test_p(self):
        a = "abc\n cde\n"
        b = "abc\n cdf\n"
        self.assertMultiLineEqual(b, a)

    def test_q(self):
        a = 2
        b = 2
        self.assertLess(a, b)

    def test_r(self):
        a = 1
        b = 2
        self.assertLessEqual(b, a)

    def test_s(self):
        a = 2
        b = 2
        self.assertGreater(b, a)

    def test_t(self):
        a = 2
        b = 1
        self.assertGreaterEqual(b, a)

    def test_u(self):
        a = None
        self.assertIsNotNone(a)

    def test_v(self):
        a = "abc\n cde\n"
        self.assertIsNone(a)

    def test_w(self):
        a = "abc"
        self.assertIsInstance(a, int)

    def test_x(self):
        a = 2
        self.assertNotIsInstance(a, int)

    def test_y(self):
        with self.assertRaisesRegexp(ValueError, 'literal1'):
            int('XYZ')

    def test_z(self):
        a = 'abbc'
        self.assertRegexpMatches(a, r'\w*oo\w*')

    def test_za(self):
        a = 'cool'
        self.assertNotRegexpMatches(a, r'\w*oo\w*')


if __name__ == '__main__':
    unittest.main()
