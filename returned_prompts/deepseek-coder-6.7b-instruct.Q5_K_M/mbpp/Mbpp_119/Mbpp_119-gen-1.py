
def search(arr):
  for i in range(0,len(arr),2):
    if i+1==len(arr) or arr[i] != arr[i+1]:
      return arr[i]


