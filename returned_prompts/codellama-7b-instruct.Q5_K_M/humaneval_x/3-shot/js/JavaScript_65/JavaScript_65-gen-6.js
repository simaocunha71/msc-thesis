  let num_digits = String(x).length;
  let result = String(x);

  if (shift >= num_digits) {
    return result.split('').reverse().join('');
  }

  result = result.split('').slice(shift).join('');
  result += result.split('').slice(0, shift).join('');

  return result;
}



