  let reversed = string.split('').reverse().join('');
  for (let i = 0; i < reversed.length; i++) {
    if (reversed.slice(i).split('').reverse().join('') === string) {
      return string + reversed.slice(0, i).split('').reverse().join('');
    }
  }
  return string + reversed;
}