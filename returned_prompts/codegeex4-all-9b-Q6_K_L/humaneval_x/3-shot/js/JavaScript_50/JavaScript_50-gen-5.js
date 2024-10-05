  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 + 26 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}