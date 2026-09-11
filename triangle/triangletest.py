import unittest
from triangle import classify_triangle


class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "scalene")

    def test_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), "scalene right")

    def test_invalid(self):
        self.assertEqual(classify_triangle(1, 2, 3), "not a triangle")


if __name__ == "__main__":
    unittest.main()