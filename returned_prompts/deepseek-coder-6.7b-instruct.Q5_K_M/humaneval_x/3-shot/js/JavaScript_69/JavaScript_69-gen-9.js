  let counts = {};
  for(let i = 0; i < lst.length; i++) {
    if(counts[lst[i]] === undefined) {
      counts[lst[i]] = 1;
    } else {
      counts[lst[i]]++;
    }
  }
  for(let i = lst.length; i > 0; i--) {
    if(counts[i] !== undefined && counts[i] >= i) {
      return i;
    }
  }
  return -1;
}



