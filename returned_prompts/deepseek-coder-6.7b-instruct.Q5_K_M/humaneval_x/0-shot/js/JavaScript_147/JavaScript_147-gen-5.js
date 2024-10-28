  let triples = 0;

  for (let i = 1; i <= n; i++) {
    for (let j = i + 1; j <= n; j++) {
      for (let k = j + 1; k <= n; k++) {
        let sum = i ** 2 - i + 1 + j ** 2 - j + 1 + k ** 2 - k + 1;
        if (sum % 3 === 0) {
          triples++;
        }
      }
    }
  }

  return triples;
}

console.log(getMaxTriples(5))

// Output: 1

// Explanation: The only valid triple is (1, 7, 13)
// 1^2 - 1 + 3^2 - 3 + 5^2 - 5 = 1 + 8 + 24 = 33, which is not a multiple of 3.
// 1 * 3 * 7 = 21, which is not a multiple of 3.
// 3 * 7 * 13 = 219, which is not a multiple of 3.
// 7 * 13 * 21 = 1269, which is not a multiple of 3.
// 13 * 21 * 33 = 3809, which is not a multiple of 3.
// So there are no valid triples.
// 
// For n = 5, a = [1, 3, 7, 13, 21], the valid triple is (1, 7, 13).
// 1 * 7 * 13 = 181, which is a multiple of 3. So there is 1 valid triple.
// 
// For n = 6, a = [1, 3, 7, 13, 21, 31], the valid triples are (1, 7, 13), (3, 7, 21), and (7, 13, 31).
// 1 * 7 * 13 = 181, 3 * 7 * 21 = 219, 7 * 1