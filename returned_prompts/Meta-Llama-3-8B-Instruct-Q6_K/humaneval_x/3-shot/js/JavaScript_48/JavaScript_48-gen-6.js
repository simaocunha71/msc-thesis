  var reversed_text = text.split("").reverse().join("");
  return text.toLowerCase() === reversed_text.toLowerCase();
}