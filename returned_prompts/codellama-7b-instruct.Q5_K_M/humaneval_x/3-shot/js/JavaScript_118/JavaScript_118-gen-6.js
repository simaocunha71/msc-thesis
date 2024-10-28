  for (let i = 0; i < word.length - 1; i++) {
    if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u') {
      if (word[i + 1] == 'b' || word[i + 1] == 'c' || word[i + 1] == 'd' || word[i + 1] == 'f' || word[i + 1] == 'g' || word[i + 1] == 'h' || word[i + 1] == 'j' || word[i + 1] == 'k' || word[i + 1] == 'l' || word[i + 1] == 'm' || word[i + 1] == 'n' || word[i + 1] == 'p' || word[i + 1] == 'q' || word[i + 1] == 'r' || word[i + 1] == 's' || word[i + 1] == 't' || word[i + 1] == 'v' || word[i + 1] == 'w' || word[i + 1] == 'x' || word[i + 1] == 'y' || word[i + 1] == 'z') {
        return word[i];
      }
    }
  }
  return '';
}



