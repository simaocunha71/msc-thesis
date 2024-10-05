  let new_string = '';
  let lower = 'abcdefghijklmnopqrstuvwxyz';
  let upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    if (lower.includes(c)) {
      new_string += upper[lower.indexOf(c)];
    } else if (upper.includes(c)) {
      new_string += lower[upper.indexOf(c)];
    } else {
      new_string += c;
    }
  }

  if (new_string.match(/[a-zA-Z]/)) {
    return new_string;
  } else {
    return new_string.split('').reverse().join('');
  }
}