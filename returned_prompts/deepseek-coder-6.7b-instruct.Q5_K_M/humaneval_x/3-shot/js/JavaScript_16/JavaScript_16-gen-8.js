  let set = new Set();
  for(let i = 0; i < string.length; i++) {
    set.add(string[i].toLowerCase());
  }
  return set.size;
}



