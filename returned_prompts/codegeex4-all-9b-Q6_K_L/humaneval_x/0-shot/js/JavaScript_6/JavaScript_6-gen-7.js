```js
const parseNestedParens = (paren_string) => {
  var groups = paren_string.split(' ');
  var depths = [];
  for (var group of groups) {
    var depth = 0;
    var max_depth = 0;
    for (var char of group) {
      if (char === '(') {
        depth += 1;
        if (depth > max_depth) {
          max_depth = depth;
        }
      } else if (char === ')') {
        depth -= 1;
      }
    }
    depths.push(max_depth);
  }
  return depths;
}
```