import unittest
from utils import p, calculateRunTime


def multiplesof3and5(to):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
    https://projecteuler.net/problem=1
    """
    sum = 0
    for i in range(1, to):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum


def sum_of_divisible(n, div):
    top = n / div
    return (top + 1) * top / 2 * div


def multiplesof3and5optimized(to):
    """
    Optimized solution to find multiples sum
    :param to:
    :return:
    """
    return sum_of_divisible(to - 1, 5) - sum_of_divisible(to - 1, 15) + sum_of_divisible(to - 1, 3)


def make_test(num):
    """
    :param num: is used to pass some variable and run tests accordingly
    :return: TestClass for unittesting
    """

    class TestClass(unittest.TestCase):
        def test(self):
            """         Unit test suite        """
            ''' testing multiplesof3and5 '''
            self.assertEqual(multiplesof3and5(3), 0)
            self.assertEqual(multiplesof3and5(4), 3)
            self.assertEqual(multiplesof3and5(10), 23)
            self.assertEqual(multiplesof3and5(1000), 233168)
            # self.assertEqual(multiplesof3and5(100000000), 2333333316666668)
            # self.assertEqual(multiplesof3and5(200000000L), 2333333316666668L)
            ''' testing multiplesof3and5optimized '''
            self.assertEqual(multiplesof3and5optimized(3), 0)
            self.assertEqual(multiplesof3and5optimized(4), 3)
            self.assertEqual(multiplesof3and5optimized(10), 23)
            self.assertEqual(multiplesof3and5optimized(1000), 233168)
            self.assertEqual(multiplesof3and5optimized(100000000), 2333333316666668)
            self.assertEqual(multiplesof3and5optimized(200000000), 9333333166666668)
            self.assertEqual(multiplesof3and5optimized(1000000000), 233333333166666668)
            ''' testing sum_of_divisible '''
            self.assertEqual(sum_of_divisible(4, 5), 0)
            self.assertEqual(sum_of_divisible(10, 5), 15)

        def test_performance(self):
            # Performance test. Method 1. Convenient and nice
            p(True)
            multiplesof3and5(30000000)
            p()

            # Performance test. Method 2.
            timer, result = calculateRunTime(multiplesof3and5, 30000000)
            print timer

            p(True)
            multiplesof3and5optimized(100000000)
            p()

        test.__doc__ = 'Test on calculations <%d>' % num

    return TestClass


Test1 = make_test(0)
# globals()['Test2'] = make_test(10)
if __name__ == '__main__':
    unittest.main(verbosity=5)