def Diff(li1, li2):
  return [i for i in li1+li2 if not i in li1 or not i in li2]