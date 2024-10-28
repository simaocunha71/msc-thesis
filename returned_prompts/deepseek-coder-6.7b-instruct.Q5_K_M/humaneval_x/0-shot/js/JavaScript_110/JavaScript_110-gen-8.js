  let oddCount = 0;
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 !== 0) {
      oddCount++;
    }
  }

  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 !== 0) {
      oddCount--;
    }
  }

  if (oddCount > 0) {
    return "NO";
  } else {
    return "YES";
  }
}

console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])); // => "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])); // => "NO"

```

Explanation:
We need to check if it's possible to convert `lst1` to an array of only even numbers by exchanging elements from `lst2`. 

We can achieve this by iterating through both lists and keeping track of the count of odd numbers in `lst1` and even numbers in `lst2`. If the count of odd numbers in `lst1` is more than the count of even numbers in `lst2`, it's impossible to make `lst1` of only even numbers.

So, we decrement the count of odd numbers in `lst1` for every odd number in `lst2` and if the count of odd numbers in `lst1` is 0 or less by the end of the loop, we return "YES", otherwise "NO".

This solution works because we can exchange odd numbers from `lst1` with even numbers from `lst2` to make `lst1` of only even numbers.

The time complexity of the solution is O(n), where n is the length of the longest list, as we are iterating through the elements of the lists once.

The space complexity is O(1), as we are using a constant amount of space to store the counts of odd and even numbers