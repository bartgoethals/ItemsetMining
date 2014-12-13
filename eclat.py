class Eclat:

   def __init__(self):
     self.f = {}

   def iProject(self, itids, items):
      """ creates the i-projected database by interstecting all tid-lists with the tid-list of i """ 
      projection = [] 
      for j, jtids in items:
         ijtids = itids & jtids
         if len(ijtids) >= minsup:
            projection.append((j,ijtids))
      return project
  
  def run(self, items, prefix=[]):
     items.sort(key=lambda item: len(item[1]), reverse=True)
     while items:
        i, itids = items.pop()
        f[str(prefix+[i])] = len(itids)
        suffix = iProject(itids, items)
        run(suffix, prefix+[i])

  def print(self):
     print(f)
