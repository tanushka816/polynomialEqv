class Checker:
    OPER = ['+', '-', '/', '*', '^']

    def __init__(self, mon):
        self.pollyn = mon.replace(' ', '')

    def new_view(self):
        if not self.pollyn:
            return ''
        res = self.pollyn[0]
        for char in self.pollyn[1:]:
            if (res[-1].isdigit() or res[-1].isalpha() or res[-1] == ')' ) and \
            (char.isdigit() or char.isalpha() or char == '('):
                if not (res[-1].isdigit() and char.isdigit()):
                    res += '*'
            res += char

        self.pollyn = res
        return res

    def check_first(self):
        op = self.pollyn
        return not (op.startswith('*') or op.startswith('/') or op.startswith('^'))

    def check_end(self):
        op = self.pollyn[-1]
        return not (op in Checker.OPER)

    def check_brackets(self):
        s = []
        for e in self.pollyn:
            if e == '(':
                s.append('(')
            elif e == ")":
                if len(s) == 0:
                    return False
                else:
                    flag = s.pop()
                    if not flag == '(':
                        return False
        return (len(s) == 0)

    def check_oper(self):
        for e in range(len(self.pollyn) - 1):
            if (self.pollyn[e] in Checker.OPER) and (self.pollyn[e+1] in Checker.OPER):
                return False
            if (self.pollyn[e] == '^' or self.pollyn[e] == '/') and (self.pollyn[e+1].isalpha()):
                return False
            if ((self.pollyn[e] == '^') or (self.pollyn[e] == '/')) and (self.pollyn[e+1] == '('):
                j = e + 2
                while not self.pollyn[j] == ')':
                    if self.pollyn[j].isalpha():
                        return False
                    j += 1
        return True

    def assert_notation_is_correct(self):
        return (self.check_oper() and
                self.check_brackets() and
                self.check_first() and
                self.check_end())