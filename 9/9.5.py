#类的常用内置函数


def test_1():

    """
    判断实例
    """

    class Myclass:
        """
        """
        __Occupation = "scientist"
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def getOccupation(self):
            return self.__Occupation

        @property
        def Occupation_property(self):
            return self.__Occupation

        
        @Occupation_property.setter
        def Occupation_property(self, value):
            if (value != "inventor") and (value != "scientist"):
                raise ValueError("Occupation_property must be inventor or scientist")
            else:
                self.__Occupation = value


    class Girlrecord(Myclass):
        """

        """

        def getOccupation(self):
            print("ok")
            print(super().getOccupation())




    myc = Myclass("ANNA", 456)
    print(myc.getOccupation())
    print(myc.Occupation_property)

    myc._Myclass__Occupation = " new dancer"
    print(myc.__dict__)
    print(myc.getOccupation())
    print(myc.Occupation_property)

    print(Myclass.__dict__)

    myc.Occupation_property = "inventor"
    print(myc.Occupation_property)


    print("*"*100)
    print(isinstance(myc, Myclass))
    print("类内置函数:isinstance, 判断object是否是class_name的实例对象")

    
    myc2 = Girlrecord("joy", 25)
    myc2.getOccupation()

    print(isinstance(myc2, Myclass))
    print("isinstance 还可以判断是否是派生类")

    print(issubclass(Girlrecord, Myclass))
    print("issubclass, 判断是否是子类")
    
    
    print(hasattr(myc, "name"))
    print("hasattr 针对实例对象,判断是否存在属性")

    print(getattr(myc, "name"))
    print(getattr(myc, "age"))
    print(getattr(myc2, "_Myclass__Occupation"))
    print(getattr(myc, "_Myclass__Occupation"))

    print("setattr 设置类实例中的某个属性")
    print(getattr(myc, "name", setattr(myc, "name", "anna_2")))
    print(myc.__dict__)
    







if __name__ == "__main__":

    test_1()