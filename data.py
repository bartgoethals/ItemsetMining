#! /usr/bin/env python
""" 
author: Bart Goethals

This class contains the necessary code to read the data in memory in a simple data structure.
This can be based on the tid-lists, diff-sets, or even simple transactions as being used by
most frequent itemset mining algorithms
"""

class Data:

  def __init__(self):
    self.data = {}
    self.trans = 0

  def readTidLists(self, filename):
    f = open(filename, 'r')
    for row in f:
      s = row.strip().split(' ')
      self.trans+=1
      for item in s:
        if item not in self.data:
          self.data[item] = set()
        self.data[item].add(self.trans)
    f.close()
