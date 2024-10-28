Here is the solution using JavaScript:

```javascript
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (String(arr[i]).length <= 2) {
      sum += arr[i];
    } else {
      break;
    }
  }
  return sum;
};
```

Explanation:
The function `addElements` takes an array `arr` and an integer `k` as inputs. It initializes a variable `sum` to 0, which will store the sum of the elements with at most two digits from the first `k` elements of `arr`.

The function then iterates through the first `k` elements of `arr` using a for loop. For each element, it checks if the length of the string representation of the element is less than or equal to 2 using `String(arr[i]).length <= 2`. If the condition is true, it adds the element to the `sum`. If the condition is false, it breaks out of the loop.

Finally, the function returns the `sum`.

In the example provided, `arr = [111,21,3,4000,5,6,7,8,9]` and `k = 4`. The function will iterate through the first 4 elements of `arr`, which are 111, 21, 3, and 4000. The elements 21 and 3 have at most two digits, so they will be added to the `sum`. The function will return `24`, which is the sum of 21 and 3.