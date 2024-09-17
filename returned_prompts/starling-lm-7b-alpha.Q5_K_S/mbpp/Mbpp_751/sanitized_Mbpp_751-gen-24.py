def check_min_heap(heap: list) -> bool:
  if len(heap) == 0:
    return True
  for i in range(len(heap)//2):
    if heap[i] > heap[2*i+1]:
      return False
    if i*2+1 != len(heap)-1 and heap[i] > heap[2*i+2]:
      return False
  return True