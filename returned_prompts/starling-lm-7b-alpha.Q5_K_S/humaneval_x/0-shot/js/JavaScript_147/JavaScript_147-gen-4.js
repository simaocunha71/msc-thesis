/*
The above solution has a time complexity of O(n^2). We can further optimize this solution to O(n) as follows:

We can precompute an array `modulo3` of size `n + 1` such that `modulo3[i]` contains the remainder of `i * i - i + 1` divided by 3. This can be computed in O(n) time using a simple loop. Then, we can iterate through `modulo3` and count the number of triples that add up to a multiple of 3.

Here is the optimized solution:
*/

const getMaxTriples = (n) => {
  let modulo3 = new Array