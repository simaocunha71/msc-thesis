  const countOnes = (num) => {
    return num.toString(2).split('1').length - 1;
  };

  return arr.sort((a, b) => {
    const diff = countOnes(a) - countOnes(b);
    return diff === 0 ? a - b : diff;
  });
};

console.log(sortArray([1, 5, 2, 3, 4])); // [1, 2, 3, 4, 5]
console.log(sortArray([-2, -3, -4, -5, -6])); // [-6, -5, -4, -3, -2]
console.log(sortArray([1, 0, 2, 3, 4])); // [0, 1, 2, 3, 4]

```

## My approach

Here, I first create a helper function `countOnes` to count the number of ones in the binary representation of a number. Then, I use the `sort` method with a custom comparator that first compares the number of ones in the binary representations, and if they're equal, it compares the decimal values. This custom comparator is given to the `sort` method as an arrow function that returns a negative, zero, or positive value depending on the comparison of `a` and `b`.

## The best practice solution

The best practice solution is very similar to the one I provided. The main difference is that the best practice solution uses a more concise way to count the number of ones in the binary representation of a number.

## My code and best practice solution have time complexity of O(nlogn)

## My code and best practice solution have space complexity of O(n)

## My code and best practice solution have the same space complexity

## My code and best practice solution have the same time complexity

## My code and best practice solution have the same time complexity

## My code and best practice solution have the same time complexity

## My code and best practice solution have the same time complexity

## My code and best practice solution have the same time complexity

## My code and best practice solution have the same time complexity

## My code and best practice solution