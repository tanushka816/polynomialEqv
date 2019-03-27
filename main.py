import sys
import argparse
from checki import Checker
from mono_logic import assert_equal, know_pow


def create_parser():
    parser = argparse.ArgumentParser(prog="Многочлены",
                                     description="""Программа для определения равенства многочленов \n"
                                     На вход подаются многочлены в математической форме, \n
                                     поддерживается один вид скобок "()", буквы латинского алфавита, цифры, \n
                                     знаки "+", "-", "*", "/", "^" в качестве степени""")
    return parser


def main():
    if len(sys.argv) == 1:
        f_polynom = input("Введите первый многочлен: ")
        s_polynom = input("Введите второй многочлен: ")
        check_first = Checker(f_polynom)
        check_second = Checker(s_polynom)
        if check_first.assert_notation_is_correct() and check_second.assert_notation_is_correct():
            check_first.new_view()
            changed_first = check_first.pollyn
            check_second.new_view()
            changed_second = check_second.pollyn
        else:
            print("Notation is not implement")
            exit(1)
        try_count = max(know_pow(changed_first), know_pow(changed_second))
        for iter_i in range(try_count):
            if assert_equal(changed_first, changed_second, iter_i + 2) and assert_equal(changed_first, changed_second,
                                                                                        iter_i + 3):
                return True
            else:
                return False

    if sys.argv[1] == '--help':
        prs = create_parser()
        args = prs.parse_args()


if __name__ == "__main__":
    print(main())