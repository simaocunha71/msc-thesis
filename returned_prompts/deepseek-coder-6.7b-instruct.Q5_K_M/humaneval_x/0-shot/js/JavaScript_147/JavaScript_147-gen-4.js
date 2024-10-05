  let count = 0;
  const arr = [];

  for (let i = 1; i <= n; i++) {
    arr.push((i * i) - i + 1);
  }

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        if ((arr[i] + arr[j] + arr[k]) % 3 === 0) {
          count++;
        }
      }
    }
  }

  return count;
};

console.log(getMaxTriples(5)); // 1
console.log(getMaxTriples(6)); // 4

```

**Explanation:**
This problem involves creating an array based on a given formula and then checking every possible combination of three numbers in the array to see if their sum is divisible by 3. 

We initialize an array `arr` and populate it with the values according to the formula `(i * i) - i + 1`, where `i` is the index of the array. We then iterate over the array to find all possible combinations of three numbers. For each combination, we check if the sum of the three numbers is divisible by 3. If it is, we increment the counter. Finally, we return the counter which holds the number of valid combinations.

This solution has a time complexity of O(n^3) due to the three nested loops.

The given examples show that the function works correctly. It returns the expected output for the given inputs.


**Optimization:**
The given solution is correct, but it can be optimized. The time complexity can be reduced to O(n^2) by using the concept of prefix sum and prefix count.

We can create another array `prefixSum[]` where `prefixSum[i] = (i * i) - i + 1` and another array `prefixCount[]` where `prefixCount[i]` is the count of numbers in `prefixSum[]` up to `i`.

Then, for each `j` and `k` such that `j < k`, we can calculate