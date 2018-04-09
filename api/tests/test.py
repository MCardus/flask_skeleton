"""App tests"""

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        """What happens before the test"""
        pass

    def test_df_to_confdict(self):
        """
        My test explanation
        :return:
        """
        self.assertEqual("1","1")

    def tearDown(self):
        """What happens after the test"""
        pass


if __name__ == '__main__':
    unittest.main()
