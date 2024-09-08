  let result = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] == ' ') {
      result += ' ';
    } else {
      let min = s[i].charCodeAt(0);
      for (let j = i + 1; j < s.length; j++) {
        if (s[j] != ' ') {
          let current = s[j].charCodeAt(0);
          if (current < min) {
            min = current;
          }
        }
      }
      result += String.fromCharCode(min);
    }
  }
  return result;
}



