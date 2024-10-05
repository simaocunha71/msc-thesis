  let distinctChars = new Set();
  for(let i = 0; i < string.length; i++){
    distinctChars.add(string[i].toLowerCase());
  }
  return distinctChars.size;
}



