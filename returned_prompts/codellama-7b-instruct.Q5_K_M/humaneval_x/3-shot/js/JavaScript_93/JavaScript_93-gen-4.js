  let encoded = "";

  for (let i = 0; i < message.length; i++) {
    if (message[i] == "a" || message[i] == "A") {
      encoded += message[i].toUpperCase();
    } else if (message[i] == "e" || message[i] == "E") {
      encoded += message[i+2].toUpperCase();
    } else if (message[i] == "i" || message[i] == "I") {
      encoded += message[i+4].toUpperCase();
    } else if (message[i] == "o" || message[i] == "O") {
      encoded += message[i+5].toUpperCase();
    } else if (message[i] == "u" || message[i] == "U") {
      encoded += message[i+7].toUpperCase();
    } else if (message[i] == " " || message[i] == "-") {
      encoded += message[i];
    } else if (message[i] == "t" || message[i] == "T") {
      encoded += message[i].toLowerCase();
    } else if (message[i] == "s" || message[i] == "S") {
      encoded += message[i+2].toLowerCase();
    } else if (message[i] == "h" || message[i] == "H") {
      encoded += message[i+4].toLowerCase();
    } else if (message[i] == "k" || message[i] == "K") {
      encoded += message[i+5].toLowerCase();
    } else if (message[i] == "m" || message[i] == "M") {
      encoded += message[i+7].toLowerCase();
    } else if (message[i] == "g" || message[i] == "G") {
      encoded += message[i+9].toLowerCase();
    } else {
      encoded += message[i];
    }
  }

  return encoded;
}



