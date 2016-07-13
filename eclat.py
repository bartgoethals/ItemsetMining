class Eclat:
   
   def __init__(self, l, ms):
     self.f = {}
     self.f[str([])]=l
     self.minsup = ms

   def iProject(self, itids, items):
      """ creates the i-projected database by interstecting all tid-lists with the tid-list of i """ 
      projection = [] 
      for j, jtids in items:
         ijtids = itids & jtids
         if len(ijtids) >= self.minsup:
            projection.append((j,ijtids))
      return projection
  
   def run(self, items, prefix=[]):
      items.sort(key=lambda item: len(item[1]), reverse=True)
      while items:
         i, itids = items.pop()
         self.f[str(sorted(prefix+[i]))] = len(itids)
         suffix = self.iProject(itids, items)
         self.run(suffix, prefix+[i])

   def rules(self):
      for i in self.f:
	for h,t in self.powerset(eval(i)):
          print str(h).strip('[]'),'=>',str(t).strip('[]'),':',self.f[i],float(self.f[i])/float(self.f[str(h)]) 

   def powerset(self,elements):
      if len(elements) > 0:
         head = elements[0]
         for h,t in self.powerset(elements[1:]):
            yield h, [head] + t
            yield [head]+h, t
      else:
         yield [],[]

   def write(self):
      for i in self.f:
         print i, ':', self.f[i]

