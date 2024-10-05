```java
const fruitDistribution = (s, n) => {
  var arr = s.split(' ');
  var a = parseInt(arr[0]);
  var o = parseInt(arr[4]);
  return n - a - o;
}
```