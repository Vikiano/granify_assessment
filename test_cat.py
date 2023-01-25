import unittest
from Cat import Cat

import unittest
from Cat import Cat

class TestCat(unittest.TestCase):
    def test_initial_age(self):
        cat = Cat()
        self.assertTrue(5 <= cat.getAge() <= 10)

    def test_speak(self):
        cat = Cat()
        self.assertEqual(cat.speak("Hello, I am a cat."), None)

    def test_getNames(self):
        cat = Cat("Whiskers")
        cat.setName("Garfield")
        cat.setName("Tom")
        self.assertEqual(cat.getNames(), ["Whiskers", "Garfield", "Tom"])

    def test_getAverageNameLength(self):
        cat = Cat("Whisker")
        cat.setName("Garfield")
        cat.setName("Tom")
        self.assertEqual(cat.getAverageNameLength(), 6.0)

if __name__ == '__main__':
    unittest.main()
