#!/usr/bin/env python3

import data
import eclat

d = data.Data()
d.readTidLists('test.dat')
e = eclat.Eclat(d.data, 2)
e.run()
e.print()
