#!/usr/bin/env python3

import data
import eclat

d = data.Data()
l = d.readTidLists('test.dat')
e = eclat.Eclat(l,2)
e.run(d.data)
e.write()
e.rules()
