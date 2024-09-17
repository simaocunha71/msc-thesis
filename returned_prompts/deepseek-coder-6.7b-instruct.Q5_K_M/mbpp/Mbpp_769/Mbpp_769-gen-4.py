
def Diff(li1, li2): 
  return [i for i in li1 + li2 if i not in li1 or i not in li2]


