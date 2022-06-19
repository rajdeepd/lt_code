import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockFoo = threading.Lock()
        self.lockFoo.acquire()
        self.lockBar = threading.Lock()

    def foo(self, printFoo):
        for i in range(self.n):
            self.lockBar.acquire() # make sure 'Bar' has been printed out before, and prevend any more print before printing 'Foo' first
            printFoo()
            self.lockFoo.release() # release so we can print 'Foo' next


    def bar(self, printBar):
        for i in range(self.n):
            self.lockFoo.acquire() # make sure 'Foo' has been printed out before, and prevend any more print before printing 'Bar' first
            printBar()
            self.lockBar.release() # release so we can print 'Bar' next