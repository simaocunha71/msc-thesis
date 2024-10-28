  let reversed = string.split('').reverse().join('');
  for (let i = 0; i < reversed.length; i++) {
    let postfix = reversed.substring(i);
    if (postfix == postfix.split('').reverse().join('')) {
      return string + postfix.split('').reverse().join('');
    }
  }
  return string + reversed;
}