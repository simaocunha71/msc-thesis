  let reversed = "";
  for (let i = 0; i < s.length; i++) {
    let code = s.charCodeAt(i);
    if ((code > 64 && code < 91) || (code > 96 && code < 123)) {
      reversed += (code > 64 && code < 91) ? String.fromCharCode(code + 32) : String.fromCharCode(code - 32);
    } else {
      reversed += s[i];
    }
  }
  return reversed;
}



