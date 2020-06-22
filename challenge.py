def make_division_by(n):
    def division(number):
        return number /  n
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest
    class ClosureSuite(unittest.TestCase):
        def setUp(self):
            self.functions = {
                6 : [18,3],
                20: [100,5],
                3: [54,18],
            }
        
        def test_closure_make_division_by(self):
            for key,value in self.functions.items():
                division = make_division_by(value[1])
                self.assertEqual(key, division(value[0]))

        def tearDown(self):
            del(self.functions)
    unittest.main()