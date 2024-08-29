  let result = '';
  for (const c of s) {
    if (c == ' ') {
      result += ' ';
    } else {
      let ordered = '';
      for (let i = 0; i < c.length; i++) {
        let min_ascii = 128;
        for (let j = i; j < c.length; j++) {
          if (c.charCodeAt(j) < min_ascii) {
            min_ascii = c.charCodeAt(j);
          }
        }
        ordered += String.fromCharCode(min_ascii);
      }
      result += ordered;
    }
  }
  return result;
}



