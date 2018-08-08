import unittest
from signup import Signup

class TestSignup(unittest.TestCase):
    def setUp(self):
        self.user1 = Signup('daniel', 'nuwa', 'daniel@gmail.com')
        self.user2 = Signup('jose','bugingo', 'jose@gmail.com')

    def test_class_created(self):
        self.assertIsInstance(self.user1, Signup)

    def test_combine_names(self):
        result = self.user1.combined_name()
        self.assertEqual(result, {'daniel nuwa'}) 

    def test_submit(self):         
        result = self.user1.submit()
        self.assertEqual(result, [{'first_name':'daniel','last_name':'nuwa', 'email':'daniel@gmail.com'}])
        self.assertIsInstance(result, list)

    def test_validate_email(self):         
        result = self.user1.validate_email('daniel@gmail.com')
        self.assertTrue(result)

if __name__ =='__main__':
    unittest.main()