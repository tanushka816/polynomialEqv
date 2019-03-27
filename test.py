import unittest
from mono_logic import assert_equal, know_pow
from checki import Checker


def fill_source(polynomial1, polynomial2):
    check_first = Checker(polynomial1)
    check_second = Checker(polynomial2)
    if check_first.assert_notation_is_correct() and check_second.assert_notation_is_correct():
        check_first.new_view()
        changed_first = check_first.pollyn
        check_second.new_view()
        changed_second = check_second.pollyn
    else:
        return "Notation is not implement"
    try_count = max(know_pow(changed_first), know_pow(changed_second))
    for iter_i in range(try_count):
        if assert_equal(changed_first, changed_second, iter_i + 2) and \
                assert_equal(changed_first, changed_second, iter_i + 3):
            return True
        else:
            return False


def get_information(file_name):
    with open(file_name, mode='r', encoding='cp1251') as f:
        final_str = f.read()
    return final_str


class TestGo(unittest.TestCase):

    #True
    def test_example_polynomial(self):
        self.assertEqual(str(fill_source("b+a", "a+b")), get_information("test_1.txt"))
    #False
    def test_ex_2(self):
        self.assertEqual(str(fill_source("x+2y", "y+2x")), get_information("test_2.txt"))

    def test_different_polynom(self):
        self.assertEqual(str(fill_source("1a", "1")), get_information("test_2.txt"))

    #ERRORS:
    def test_var_division(self):
        self.assertEqual(str(fill_source("6/c", "24")), get_information("test_3.txt"))

    def test_error_first_element(self):
        self.assertEqual(str(fill_source("*6", "24")), get_information("test_3.txt"))

    def test_error_last_element(self):
        self.assertEqual(str(fill_source("6+", "24")), get_information("test_3.txt"))

    def test_error_bracket(self):
        self.assertEqual(str(fill_source("())(", "24")), get_information("test_3.txt"))

    def test_error_operations(self):
        self.assertEqual(str(fill_source("24+-5", "24")), get_information("test_3.txt"))


if __name__ == "__main__":
    unittest.main()
