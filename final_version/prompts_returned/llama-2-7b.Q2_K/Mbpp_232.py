"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""
from typing import Any, Callable, Dict, List, Optional, Tuple
import csv
import functools
import operator
from typing import Generic

class MaxHeap:
    def __init__(self):
        self.max_heap = []

    def _insert(self, value):
        pass

    def popmin(self):
        pass

class PriorityQueue:
    def __init__(self):
        self._pq = [None for _ in range(32)]

    def push(self, item):
        current_size = len(self._pq) + 1
        if self._pq[current_size] is None:
            self._pq[current_size] = item
        else:
            raise ValueError("Duplicate Priority")
        return current_size

    def pop(self):
        pass

class MaxHeap