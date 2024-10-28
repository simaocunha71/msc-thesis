  let result = [];

  for (let i = 0; i < x.length; i++) {
    let hasEvenDigit = false;
    let num = x[i].toString();

    for (let j = 0; j < num.length; j++) {
      if (num[j] % 2 === 0) {
        hasEvenDigit = true;
        break;
      }
    }

    if (!hasEvenDigit) {
      result.push(x[i]);
    }
  }

  return result.sort((a, b) => a - b);
}

uniqueDigits([15, 33, 1422, 1]); // [1, 15, 33]
uniqueDigits([152, 323, 1422, 10]); // []

```

This solution goes through each number in the list, converts it to a string, and then checks each digit. If a digit is even, it sets the `hasEvenDigit` flag to true and breaks out of the loop. If no even digits are found, it adds the number to the result array. Finally, it sorts the result array and returns it.

It has a time complexity of O(n*m) where n is the number of elements in the list and m is the number of digits in the largest number.

It has a space complexity of O(n) because it creates a new array to hold the result.


```



```python
def uniqueDigits(x):
    result = []

    for i in x:
        hasEvenDigit = False
        for j in str(i):
            if int(j) % 2 == 0:
                hasEvenDigit = True
                break

        if not hasEvenDigit:
            result.append(i)

    return sorted(result)

print(uniqueDigits([15, 33, 1422, 1]))  # Output: [1, 15, 33]
print(uniqueDigits([152, 323, 1422, 10]))  #