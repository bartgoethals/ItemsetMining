class Eclat:
   
   def __init__(self, ms):
     self.f = {}
     self.minsup = ms

   def iProject(self, itids, items):
      """ creates the i-projected database by interstecting all tid-lists with the tid-list of i """ 
      projection = [] 
      for j, jtids in items:
         ijtids = itids & jtids
         if len(ijtids) >= self.minsup:
            projection.append((j,ijtids))
      return project
  
   def run(self, items, prefix=[]):
      items.sort(key=lambda item: len(item[1]), reverse=True)
      while items:
         i, itids = items.pop()
         self.f[str(prefix+[i])] = len(itids)
         suffix = self.iProject(itids, items)
         run(suffix, prefix+[i])

   def print(self):
      print(f)
