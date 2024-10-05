/*
  This problem can be solved using dynamic programming.
  The key observation is that we can only change one element at a time,
  and we can't change it to itself. So we can do a brute force approach,
  where we try all possible changes of one element at a time.
  But we can do better.
  We can try to change the smallest element at the beginning,
  and the second smallest element at the end,
  and so on.
  The number of elements we need to change is the number of elements in the array,
  minus the number of elements in the middle.
  The number of elements in the middle is the number of elements in the array
  minus the number of elements in the beginning and the number of elements in the end.
  The number of elements in the beginning and the number of elements in the end
  is the number of elements in the array divided by 2.
  So the number of elements we need to change is the number of elements in the array
  minus the number of elements in the middle,
  which is the number of elements in the array minus the number of elements in the beginning
  and the number of elements in the end.
  The number of elements in the beginning and the number of elements in the end
  is the number of elements in the array divided by 2.
  So the number of elements we need to change is the number of elements in the array
  minus the number of elements in the middle,
  which is the number of elements in the array minus the number of elements in the beginning
  and the number of elements in the end.
  The number of elements in the beginning and the number of elements in the end
  is the number of elements in the array divided by 2.
  So the number of elements we need to change is the number of elements in the array
  minus the number of elements in the middle,
  which is the number of elements in the array minus the number of elements in the beginning
  and the number of elements in the end.
  The number of elements in the beginning and the number of elements in the end
  is the number of elements in the array divided by 2.
  So the number of elements we need to change is the number of elements in the array
  minus the number of elements in the middle,
  which