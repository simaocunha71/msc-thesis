  return s.split("").map(ch => {
    if (ch.match(/[a-zA-Z]/)) {
      return String.fromCharCode(((ch.charCodeAt(0) - "a".charCodeAt(0) + n) % 26) + "a".charCodeAt(0));
    } else {
      return ch;
    }
  }).join("");
}



