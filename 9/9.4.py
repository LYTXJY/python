#实现子类



def test_1():

    class Record:
        """
        father class
        """
        __Occupation = 'scientist'

        def __init__(self, name, age):
            self.name = name 
            self.age = age

        def showrecord(self):
            print("Occupation : ", self.getOccupation())

        def getOccupation(self):
            return self.__Occupation


    class GirlRecord(Record):
        """
        derived class 
        """
        def showrecord(self):
            Record.showrecord(self)

            #等价如下:
            super().showrecord()
            print("the girl:", self.name, "'s age is ", self.age)


    myc = GirlRecord("anna", 85)
    myc.showrecord()

    print(GirlRecord.__dict__)
    print(myc.__dict__)

    print("子类会继承父类的初始化函数,无需在额外进行初始化定义")
    print("子类可以对父类的成员函数进行覆写,从而实现全新的功能")




def test_2():
    """
    super函数

    父类的成员函数被子类调用多次, 是需要尽量避免的
    通过使用super函数来保证父类的方法只被执行一次
    super函数的本意:获得父类的对象,并调用父类的方法

    使用super函数与直接使用父类的区别是:通过super函数进行调用的父类方法,会保证只执行一次

    在复杂继承关系中,super函数会大大提高代码的可控性.
    """

    def test_2_1():
        """
        反面案例

        """
        class Record:
            """
            A record class
            """

            __Occupation = "scientist"
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def showrecord(self):
                print("Occupation : ", self.getOccupation())

            def getOccupation(self):
                return self.__Occupation


        class FemaleRecord(Record):
            """
            a girlrecord class
            """
            def showrecord(self):
                print(self.name, ":", self.age, ",female")
                Record.showrecord(self)


        class RetireRecord(Record):
            """
            a retirerecord class
            """
            def showrecord(self):
                Record.showrecord(self)
                print("retired worker")

        class ThisRecord(FemaleRecord, RetireRecord):
            """
            A Thisrecord class
            """
            def showrecord(self):
                print("the member detail as follow : ")
                FemaleRecord.showrecord(self)
                RetireRecord.showrecord(self)

        myc = ThisRecord("anna", 54)
        myc.showrecord()

        print("两个派生类,调用了父类两次")
        print("实际编程过程中,这种父类函数被自动执行多次的情况一定要避免")
        print("如果showrecord()函数中有资源申请之类的操作,会造成资源泄漏,严重影响程序的性能")


    # test_2_1()



    def test_2_2():
        """
        正面例子
        使用super函数, 实现多重继承中的父类调用
        """

        class Record:
            """
            a record class
            """
            __Occupation = "scientist"

            def __init__(self, name, age):
                self.name = name
                self.age = age

            def showrecode(self):
                print("Occupation : ", self.getOccupation())

            def getOccupation(self):
                return self.__Occupation

        class FemaleRecord(Record):
            """
            a girlrecord class
            """
            def showrecode(self):
                print(self.name, ":", self.age, ", female")
                super().showrecode()
            
        class RetireRecord(Record):
            """
            a retiredrecord class
            """
            def showrecode(self):
                super().showrecode()
                print("retired worker")

        class ThisRecord(FemaleRecord, RetireRecord):
            """
            a thisrecord class
            """
            def showrecode(self):
                print("the member detail as follow :")
                super().showrecode()


        myc = ThisRecord("aleia", 86)
        myc.showrecode()



        # myc = Record("jexika", 36)
        # myc.showrecode()


    test_2_2()





if __name__ == "__main__":
    # test_1()
    test_2()