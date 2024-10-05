
  let t = [3];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      t.push(t[i - 1]);
    } else {
      let num1 = t[t.length - 3] || 0;
      let num2 = t[t.length - 2] || 0;
      let num3 = t[t.length - 1] || 0;
      t.push(num1 + num2 + num3);
    }
  }
  return t;
};

console.log(tri(3));

*/

// Solution

function tribonacci(n) {
  let tribo = [3];
  for (let i = 2; i <= n; i++) {
    if (i % 2 === 0) {
      tribo.push(tribo[tribo.length - 1]);
    } else {
      tribo.push(
        tribo[tribo.length - 3] || 0 + tribo[tribo.length - 2] || 0 + tribo[tribo.length - 1] || 0
      );
    }
  }
  return tribo;
}

console.log(tribonacci(3));

































































































































































































