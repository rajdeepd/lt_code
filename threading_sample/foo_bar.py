import time
from threading import *

class FooBar(object):
    def __init__(self, n):
        self.n = n

    def foo(self, printFoo):
    #def foo(self):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):

            condition_object.acquire()
            printFoo()
            condition_object.notify()
            condition_object.wait()
            condition_object.release()

    def bar(self, printBar):
    #def bar(self):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            condition_object.acquire()
            #print("Bar: Waiting")
            condition_object.wait()
            printBar()
            condition_object.notify()
            condition_object.release()



condition_object = Condition()
class_obj = FooBar(10)

def printFoo():
    print("Foo")

def printBar():
    print("Bar")

T1 = Thread(target=class_obj.foo, args=(printFoo,))
T2 = Thread(target=class_obj.bar, args=(printBar,))
#T1 = Thread(target=class_obj.foo)
#T2 = Thread(target=class_obj.bar)
T2.start()
T1.start()
