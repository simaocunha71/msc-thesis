  let digits = x.toString().split('');
  let len = digits.length;

  if (shift < len) {
    let last = digits.pop();
    for (let i = 0; i < shift; i++) {
      digits.push(digits.shift());
    }
    digits.push(last);
  } else {
    digits.reverse();
  }

  return digits.join('');
}



