class First:
    cnt = 0

    def __init__(self, num):
        self.num = num

    @staticmethod
    def myfun():
        First.cnt = 23
        return First.cnt

    @classmethod
    def myfun1(cls):
        cls.cnt = 34
        print("hello\t", cls.cnt)
        del cls.cnt


f1 = First(100)
print(First.cnt)
print(f1.num, "\t", First.myfun())
print(First.cnt)
First.myfun1()

print(First.myfun())
print("\n",First.cnt)