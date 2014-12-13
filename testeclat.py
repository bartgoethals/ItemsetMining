#!/usr/bin/env python3

import data
import eclat

d = data.Data()
d.readTidLists('test.dat')
e = eclat.Eclat(2)
e.run(d.data)
e.print()
