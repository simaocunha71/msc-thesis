```java
const matchParens = (lst) => {
  var s1 = lst[0];
  var s2 = lst[1];
  var s3 = s1 + s2;
  var s4 = s2 + s1;
  var balanced1 = true;
  var balanced2 = true;
  var stack = [];

  for (var i = 0; i < s3.length; i++) {
    if (s3[i] == '(') {
      stack.push(s3[i]);
    }
    else {
      if (stack.length == 0) {
        balanced1 = false;
        break;
      }
      else {
        stack.pop();
      }
    }
  }

  if (stack.length != 0) { balanced1 = false; }

  stack = [];

  for (var i = 0; i < s4.length; i++) {
    if (s4[i] == '(') {
      stack.push(s4[i]);
    }
    else {
      if (stack.length == 0) {
        balanced2 = false;
        break;
      }
      else {
        stack.pop();
      }
    }
  }

  if (stack.length != 0) { balanced2 = false; }

  if (balanced1 == true || balanced2 == true) { return 'Yes'; }
  else { return 'No'; }
}
```
