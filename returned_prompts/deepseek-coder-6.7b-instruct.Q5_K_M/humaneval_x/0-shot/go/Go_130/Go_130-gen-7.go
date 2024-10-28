
// Solution 1: Using Recursion

// Recursive solution, however, it will have a high time complexity and will not
// work for large inputs due to the reasons mentioned in the comments.

tri := make([]float64, n+1)
for i := range tri {
  tri[i] = -1
}

var triHelper func(int) float64
triHelper = func(n int) float64 {
  if n == 0 {
    return 0
  }
  if n == 1 || n == 2 {
    return 1
  }
  if tri[n] != -1 {
    return tri[n]
  }
  tri[n] = triHelper(n-1) + triHelper(n-2) + triHelper(n+1)
  return tri[n]
}

for i := 0; i <= n; i++ {
  tri[i] = triHelper(i)
}

return tri

// Solution 2: Iterative Approach

// This approach will work for large inputs and it will have a time complexity
// of O(n).

tri := make([]float64, n+1)
switch n {
case 0:
  return tri
case 1:
  tri[1] = 1
  return tri
case 2:
  tri[1], tri[2] = 1, 1
  return tri
default:
  tri[1], tri[2], tri[3] = 1, 1, 2
  for i := 4; i <= n; i++ {
    if i%2 == 0 {
      tri[i] = 1 + float64(i)/2
    } else {
      tri[i] = tri[i-1] + tri[i-2] + tri[i+1]
    }
  }
  return tri
}

// Solution 3: Using a Generator function

// This approach uses a generator function to compute the Tribonacci sequence.
// This will also work for large inputs and it will have a time complexity of
// O(n).

func triGenerator() func() float