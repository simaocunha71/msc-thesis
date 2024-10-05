```java
const closestInteger = (value) => {
  var num = +value;
  var floor = Math.floor(num);
  var ceil = Math.ceil(num);
  if (num - floor < ceil - num) { return floor; }
  else { return ceil; }
}
```
