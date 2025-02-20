import unittest
import main as source

class RunTests(unittest.TestCase):

    def test_one(self):
        self.assertEqual(source.run_operation_add(1,1), 2)
    
    def test_two(self):
        self.assertRaises(ValueError, source.run_operation_div, 0, 2)

if __name__ == '__main__':
    unittest.main()