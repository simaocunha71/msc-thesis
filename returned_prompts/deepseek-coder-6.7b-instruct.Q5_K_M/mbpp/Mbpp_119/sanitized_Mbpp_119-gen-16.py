def search(arr):
  for i in range(0, len(arr), 2):
    if i == len(arr)-1 or arr[i] != arr[i+1]:
      return arr[i]