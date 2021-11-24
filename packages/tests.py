import unittest
import main


main.t = "main"

class MyTestCase(unittest.TestCase):
    def test_main(self):
        pass


if __name__ == '__main__':
    unittest.main()