class Calculator(object):

    def add(self, x, y):
        return x + y

    def Minus(self, X, Y):
        number_types = (int, long, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return X - Y
        else:
            raise ValueError
