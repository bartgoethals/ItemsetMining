#!/usr/bin/env python3

import data
import eclat

d = Data()
d.readTidLists('test.dat')
e = Eclat(d.data, 2)
e.run()
e.print()
