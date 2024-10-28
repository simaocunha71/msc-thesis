  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - "a".charCodeAt(0)) % 26) + 5 + "a".charCodeAt(0)
  )).join("");
}