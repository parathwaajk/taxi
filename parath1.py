
import unittest
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

class LearnTest(unittest.TestCase):

    def setUp(self):
        self.a=20
        self.b=20
    def testsum(self):
        self.assertEqual(add(self.a,self.b),self.a+self.b)
    def testsubtract(self):
        self.assertEqual(subtract(self.a,self.b),self.a-self.b)
    def testmultiply(self):
        self.assertEqual(multiply(self.a, self.b), self.a * self.b)
    def testdivide(self):
        self.assertEqual(divide(self.a, self.b), self.a/self.b)

if __name__ == '__main__':
        unittest.main(verbosity=2)