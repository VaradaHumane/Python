class A:
    def __init__(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c

    def display(self):
        print(f"a: {self.__a} b: {self._b} c: {self.c}")


class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def display(self):
        super().display()


try:
    a = A(1, 2, 3)
    print("A has: ")
    a.display()
    print("values.")

    b = B(4, 5, 6)
    print("B has: ")
    b.display()
    print("values.")

    print(a.__a)
except AttributeError:
    print("not accessible")
