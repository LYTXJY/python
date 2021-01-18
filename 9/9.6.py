#重载运算符


def test_1():
    """

    """


    class Myclass():
        """
        重载运算符
        """
        
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __str__(self):
            return "name:"+self.name + ";age:"+str(self.age)

        __repr__ = __str__

        def __lt__(self, record):
            if self.age < record.age:
                return True
            else:
                return False

        def __add__(self, record):
            return Myclass(self.name, self.age + record.age)

    myc = Myclass("anna", 58)
    myc1 = Myclass("gray", 22)

    print(repr(myc))
    print(myc)
    print(str(myc))
    print(myc<myc1)
    print(myc+myc1)




if __name__ == "__main__":
    test_1()