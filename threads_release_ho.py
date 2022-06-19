from threading import Thread
import threading
from threading import Lock, Condition

# https://leetcode.com/problems/building-h2o/
import time


class H2O(object):
    def __init__(self):
        self.oCount = 0
        self.hCount = 0
        self.cond = Condition()
        self.zero_ox = lambda : self.oCount == 0
        self.less_than_two_hyd = lambda : self.hCount < 2


    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        with self.cond:
            self.cond.wait_for(self.less_than_two_hyd)
            self.hCount += 1
            releaseHydrogen()
            self.try_reset()
            self.cond.notifyAll()

    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """

        # releaseOxygen() outputs "O". Do not change or remove this line.
        with self.cond:
            self.cond.wait_for(self.zero_ox)
            self.oCount += 1
            releaseOxygen()
            self.try_reset()
            self.cond.notifyAll()

    def try_reset(self):
        if not self.zero_ox and not self.less_than_two_hyd:
            self.oCount = 0
            self.hCount = 0
