def assert_equal(poly1, poly2, tmp):
    poly_in_1 = poly1.replace('^', '**')
    poly_in_2 = poly2.replace('^', '**')

    random_tmp = tmp
    dict_of_vars = dict()
    for e in (poly_in_1 + poly_in_2):
        if e.isalpha():
            if e not in dict_of_vars:
                dict_of_vars[e] = random_tmp
                random_tmp += 3
            poly_in_1 = poly_in_1.replace(e, str(dict_of_vars[e]))
            poly_in_2 = poly_in_2.replace(e, str(dict_of_vars[e]))
    return eval(poly_in_1) == eval(poly_in_2)


def know_pow(poly):
    set_var = set()
    for e in poly:
        if e.isalpha():
            set_var.add(e)

    max_pow = 1
    dict_of_vars = dict.fromkeys(set_var, 0)

    for e in range(len(poly)-1):
        if poly[e].isalpha():
            if poly[e+1] == "^":
                i = e + 2
                tmp_pow = ""
                while i < len(poly) and poly[i].isdigit():
                    tmp_pow += poly[i]
                    i += 1
                dict_of_vars[poly[e]] += int(tmp_pow)
                e += i
    for e in dict_of_vars:
        if dict_of_vars[e] > max_pow:
            max_pow = dict_of_vars[e]
    return max_pow
