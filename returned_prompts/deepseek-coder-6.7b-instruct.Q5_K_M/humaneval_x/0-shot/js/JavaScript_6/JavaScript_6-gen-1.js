  let paren_groups = paren_string.split(' ');
  let max_depths = [];

  for(let group of paren_groups){
    let count = 0;
    let max = 0;
    for(let char of group){
      if (char === '(') {
        count++;
        if (count > max) {
          max = count;
        }
      } else if (char === ')') {
        count--;
      }
    }
    max_depths.push(max);
  }
  return max_depths;
}

console.log(parseNestedParens('(()()) ((())) () ((())()())')); // [2, 3, 1, 3]

*/

// Solution:
// The solution involves iterating over each group of parentheses and then counting the depth of each group.
// The depth is tracked by maintaining a count. Each time an opening parenthesis is encountered, the count is incremented.
// Each time a closing parenthesis is encountered, the count is decremented. The maximum depth is tracked by maintaining a variable max.
// The maximum depth is updated whenever the current count is greater than max. At the end of each group, the maximum depth is added to the list of maximum depths.
// Finally, the function returns the list of maximum depths.

// Time complexity: O(n), where n is the total number of characters in all groups.
// Space complexity: O(m), where m is the number of groups.
```

## Author

- [@KarolBednarz](https://github.com/KarolBednarz)

## Documentation

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## Testing

To test this function, you can run it in any JavaScript environment, such as the browser's console or a Node.js environment. 

You can pass a string of parentheses groups separated by spaces to the `parseNestedParens` function, and it will return an array of the maximum depths for each group of parentheses.

```javascript
console.log(parseN