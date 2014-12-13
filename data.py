#! /usr/bin/env python
""" 
author: Bart Goethals

This class contains the necessary code to read the data in memory in a simple data structure.
This can be based on the tid-lists, diff-sets, or even simple transactions as being used by
most frequent itemset mining algorithms
"""

class Data:

  def __init__(self):
    self.data = []

  def readTidLists(self, filename):
    trans = 0
    d = {}
    f = open(filename, 'r')
    for row in f:
      s = row.strip().split(' ')
      trans+=1
      for item in s:
        if item not in d:
          d[item] = set()
        d[item].add(trans)
    f.close()
    self.data = sorted(d.items(), key=lambda item: len(item[1]), reverse=True)
