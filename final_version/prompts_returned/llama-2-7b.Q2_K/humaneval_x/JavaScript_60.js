/*sumToN is a function that sums numbers from 1 to n.
  >>> sumToN(30)
  465
  >>> sumToN(100)
  5050
  >>> sumToN(5)
  15
  >>> sumToN(10)
  55
  >>> sumToN(1)
  1
  */
const sumToN = (n) => {
  let count = 0;
  for (let i=1 ; i<=n ; i++) {count+=i;}
  console.log(count);
}