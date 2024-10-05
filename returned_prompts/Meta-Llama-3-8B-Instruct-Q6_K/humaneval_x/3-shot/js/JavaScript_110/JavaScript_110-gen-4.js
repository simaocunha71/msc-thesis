  let oddCount = 0;
  let oddNumbers = [];

  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 !== 0) {
      oddCount++;
      oddNumbers.push(lst1[i]);
    }
  }

  if (oddCount > lst2.length) {
    return "NO";
  }

  for (let i = 0; i < oddCount; i++) {
    for (let j = 0; j < lst2.length; j++) {
      if (lst2[j] % 2 !== 0) {
        lst2.splice(j, 1);
        j--;
        break;
      }
    }
  }

  return "YES";
}
// Example usage:
console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])); // Output: "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])); // Output: "NO"