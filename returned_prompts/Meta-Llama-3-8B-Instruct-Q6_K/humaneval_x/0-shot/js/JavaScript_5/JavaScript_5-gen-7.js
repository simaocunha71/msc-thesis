```
const intersperse = (numbers, delimeter) => {
  if (numbers.length === 0) {
    return numbers;
  }
  return [numbers[0], ...[delimeter].repeat(numbers.length - 1), ...numbers.slice(1)];
};
```
Explanation:
This function takes a list of numbers and a delimiter as arguments. It checks if the input list is empty, and if so, returns the list as is. If the list is not empty, it constructs a new list by concatenating the first element of the original list, the delimiter repeated `numbers.length - 1` times, and the rest of the original list (excluding the first element). The `...` operator is used to spread the arrays and concatenate them. The `repeat` method is used to create an array of the delimiter repeated the desired number of times. The `slice` method is used to get the rest of the original list. The resulting list is returned.