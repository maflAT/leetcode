"""The median is the middle value in an ordered integer list. If the size of
the list is even, there is no middle value and the median is the mean of the
two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data
    structure.
    double findMedian() returns the median of all elements so far. Answers
    within 10-5 of the actual answer will be accepted.
"""
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

from bisect import insort
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        insort(self.nums, num)

    def findMedian(self) -> float:
        center, mod = divmod(len(self.nums), 2)
        if mod == 0:
            return (self.nums[center - 1] + self.nums[center]) / 2.0
        else:
            return float(self.nums[center])
