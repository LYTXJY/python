# 类的私有化属性


def test_1():
    """
    类的私有化熟悉,解决类变量被修改的隐患
    方法有二:
    一:使用get函数,来获取私有化类变量的信息
    二:使用装饰器+私有变量方式 (最多用法)
    """

    class Myclass():
        """
        """

        __Occupation = "scientist"

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def getOccupation(self):
            return self.__Occupation

    myc = Myclass("anna", 18)
    myc1 = Myclass("joy", 56)

    print(myc.getOccupation())
    print(myc1.getOccupation())

    myc1.__Occupation = "dancer"
    print(myc1.__Occupation)
    print(myc1.getOccupation())

    print(myc.__dict__)
    print(Myclass.__dict__)
    print(Myclass._Myclass__Occupation)
    print(myc._Myclass__Occupation)

    myc._Myclass_Occupation = "cooker"
    print(myc._Myclass_Occupation)
    print(myc.getOccupation())

    print(myc.__dict__)


def test_2():
    """
    装饰器方法修饰类的私有化变量

    装饰器将类的私有变量的set与get功能集成到类的属性中去
    通过属性访问类的私有化变量信息
    """

    class Myclass():

        __Occupation = "scientist"

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def getrecode(self):
            return self.name, self.age

        def getOccupation(self):
            return self.__Occupation

        @property
        def Occupation_property(self):
            return self.__Occupation

    myc = Myclass("anna", 98)
    print(myc.getOccupation())
    print(myc.Occupation_property)


def test_3():
    """
    装饰器仅实现了类私有化变量的读取,并不能实现修改
    通过@Occupation.setter 实现类私有化变量的设置
    """

    class Myclass():
        __Occupation = "scientist"

        def __init__(self, name, age):
            self.name = name
            self.age = age

        @property
        def Occupation(self):
            return self.__Occupation

        #上述property仅仅可以通过属性的方式进行访问,无法进行设置

        @Occupation.setter
        #设置需要掀开启 property变成私有化类熟悉,再使用.setter功能给私有化类变量赋值

        def Occupation(self, value):
            if (value != "inventor") and (value != "scientist"):
                raise ValueError("Occupation must be inventor or scientist!")
            else:
                self.__Occupation = value



    myc = Myclass("qqq", 45)
    print(myc.Occupation)

    myc.Occupation = "inventor"
    print(myc.Occupation)

    # myc.Occupation = "DANCER"

if __name__ == "__main__":

    # test_1()
    # test_2()
    test_3()
