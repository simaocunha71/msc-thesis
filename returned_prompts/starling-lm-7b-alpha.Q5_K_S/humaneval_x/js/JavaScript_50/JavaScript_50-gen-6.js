  return s.split("").map(ch => {
    const base = "a".charCodeAt(0);
    const code = ch.charCodeAt(0);
    if (!('a' <= ch && ch <= 'z')) {
      return ch;
    }
    let result = (code - base + n) % 26;
    if (result < 0) result += 26;
    return String.fromCharCode(result + base);
  }).join("");
}



