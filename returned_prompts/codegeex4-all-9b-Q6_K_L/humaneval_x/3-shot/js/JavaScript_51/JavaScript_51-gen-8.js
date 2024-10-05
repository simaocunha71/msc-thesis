  var vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  var result = '';

  for (var i = 0; i < text.length; i++) {
    if (!vowels.includes(text[i])) {
      result += text[i];
    }
  }

  return result;
}



