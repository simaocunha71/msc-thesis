  let result = [1, 3];
  if (n <= 2) {
    return result.slice(0, n + 1);
  }
  let a = 1;
  let b = 3;
  let c = 2;
  for (let i = 3; i <= n; i++) {
    let temp = a + b + c;
    a = b;
    b = c;
    c = temp;
  }
  result.push(a, b, c);
  return result;
}
//console.log(tri(3)); // [1, 3, 2, 8]
//console.log(tri(5)); // [1, 3, 2, 8, 4, 11]