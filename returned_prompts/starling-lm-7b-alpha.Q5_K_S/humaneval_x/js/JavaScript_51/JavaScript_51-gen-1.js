  let vowels = "aeiouAEIOU";
  let result = "";
  for (let i = 0; i < text.length; i++) {
    if (vowels.indexOf(text[i]) == -1) {
      result += text[i];
    }
  }
  return result;
}



