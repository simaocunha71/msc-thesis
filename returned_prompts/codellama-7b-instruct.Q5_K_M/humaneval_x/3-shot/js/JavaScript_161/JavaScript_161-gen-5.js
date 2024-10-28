  let result = [];
  let is_letter = false;

  for (let c of s) {
    if (isLetter(c)) {
      is_letter = true;
      if (isLowerCase(c)) {
        result.push(c.toUpperCase());
      } else {
        result.push(c.toLowerCase());
      }
    } else {
      result.push(c);
    }
  }

  if (!is_letter) {
    result = result.reverse();
  }

  return result.join('');
}



