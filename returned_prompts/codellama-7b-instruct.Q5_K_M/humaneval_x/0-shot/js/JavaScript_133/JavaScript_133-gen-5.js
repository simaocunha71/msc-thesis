const sumSquares = (lst) => {
  var arr = [];
  for (var i = 0; i < lst.length; i++) {
    arr[i] = Math.ceil(lst[i]);
  }
  var sum = arr.reduce((a, b) => a + b);
  var result = sum * sum;
  return result;
}
