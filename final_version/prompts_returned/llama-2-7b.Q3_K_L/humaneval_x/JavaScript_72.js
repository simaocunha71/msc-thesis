/*
  Write a function that returns true if the object q will fly, and false otherwise.
  The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

  Example:
  willItFly([1, 2], 5) ➞ false
  # 1+2 is less than the maximum possible weight, but it's unbalanced.

  willItFly([3, 2, 3], 1) ➞ false
  # it's balanced, but 3+2+3 is more than the maximum possible weight.

  willItFly([3, 2, 3], 9) ➞ true
  # 3+2+3 is less than the maximum possible weight, and it's balanced.

  willItFly([3], 5) ➞ true
  # 3 is less than the maximum possible weight, and it's balanced.
  */
const willItFly = (q, w) => {
  let max = q[0];
  for (let i = 1; i < Math.max(w / max, 0); i++) {
    const sum = 0;
    for (let j = 0; j < i && j < q.length - 1; j++) {
      if (q[j] === q[i]) break;
      sum += Math.min(q[j], q[i]);
    }
    max = Math.max(sum, max);
  }
  return !((Math.abs(w - max) > w / 30) && (Math.abs(w - max) < Math.abs(w)));
};
