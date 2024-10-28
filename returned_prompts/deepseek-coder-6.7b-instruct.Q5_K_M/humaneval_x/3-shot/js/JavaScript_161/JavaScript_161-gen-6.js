  let chars = Array.from(s);

  for  (let i = 0; i < chars.length; i++) {
    if (chars[i].match(/[a-z]/i)) {
      chars[i] = chars[i] === chars[i].toUpperCase() ? chars[i].toLowerCase() : chars[i].toUpperCase();
    }
  }

  return chars.join('');
}



