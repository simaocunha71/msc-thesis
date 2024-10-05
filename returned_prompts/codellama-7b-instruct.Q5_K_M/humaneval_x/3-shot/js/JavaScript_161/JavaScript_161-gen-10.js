  let result = [];
  let is_letter = false;

  for (let c of s) {
    if (c.match(/[a-zA-Z]/)) {
      is_letter = true;
      if (c.match(/[a-z]/)) {
        result.push(c.toUpperCase());
      } else {
        result.push(c.toLowerCase());
      }
    } else {
      result.push(c);
    }
  }

  if (is_letter) {
    return result.join('');
  } else {
    return s.split('').reverse().join('');
  }
}



