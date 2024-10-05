
You are on the right track with the first problem, but there are a couple of issues with your code.
Firstly, the inner loop should start from i + 1, because you are already comparing each element with the previous ones in the outer loop.
Secondly, you don't need to check if i != j, because you are comparing each element with the next one in the inner loop.
Here's the corrected code:
```javascript
const hasCloseElements = (numbers, threshold) => {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let distance = Math.abs(numbers[i] - numbers[j]);
      if (distance < threshold) {
        return true;
      }
    }
  }
  return false;
}
```

For the second problem, you are on the right track with your approach, but there are a couple of issues with your code.
Firstly, you are using a for...of loop to iterate over the characters of the string, but you should be using a regular for loop with a counter variable to keep track of the current depth.
Secondly, you are using a while loop to iterate over the characters of the string, but you don't need to do that. You can just use a for loop to iterate over the characters of the string.
Here's the corrected code:
```javascript
const separateParenGroups = (paren_string) => {
  var result = [];
  var current_string = [];
  var current_depth = 0;

  for (let i = 0; i < paren_string.length; i++) {
    if (paren_string[i] == '(') {
      current_depth += 1;
      current_string.push(paren_string[i]);
    } else if (paren_string[i] == ')') {
      current_depth -= 1;
      current_string.push(paren_string[i]);
      if (current_depth == 0) {
        result.push(current_string.join(''));
        current_string = [];
      }
    }
  }

  return result;
}
```

For the third problem, you are on the right track with your approach, but there are a couple of