const skjkasdkd = (lst) => {
const arr = lst.filter(x => {
  const prime = isPrime(x);
  if (prime) return prime;
});
const num = Math.max(...arr);
const sum = num.toString().split("").reduce((acc, curr) => {
  return acc + +curr;
}, 0);
return sum;
};

