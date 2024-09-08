  let vowels = ["a","e","i","o","u","A","E","I","O","U"];
  let result = "";
  for (let i = 0; i < text.length; i++) {
    if (!vowels.includes(text[i])) {
      result += text[i];
    }
  }
  return result;
}



