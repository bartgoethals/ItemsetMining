import data

class Eclat:

   def __init__(self):
     self.f = {}

   def iProject(self, items, prefix=[]):
     i, itids = items.pop()
     isupp = len(itids)
     suffix = [] 
     for j, ojtids in items:
        jtids = itids & ojtids
        jsupp = len(jtids)
        if jsupp >= minsup:
          suffix.append((j,jtids))
     return suffix
  
  def run(self, items, prefix=[]):
        while items:
            run(suffix, prefix+[i]+closure)
