  let distinctCharacters = new Set();
  for  (let i = 0; i < string.length; i++)  {
    distinctCharacters.add(string[i].toLowerCase());
  }
  return distinctCharacters.size;
}



