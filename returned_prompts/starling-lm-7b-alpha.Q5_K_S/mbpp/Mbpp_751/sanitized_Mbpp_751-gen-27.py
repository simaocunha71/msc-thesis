def check_min_heap(heap):
  for i in range(len(heap)):
    if i*2 + 1 < len(heap):
      if heap[i] > heap[i*2 + 1]:
        return False
    if i*2 + 2 < len(heap):
      if heap[i] > heap[i*2 + 2]:
        return False
  return True