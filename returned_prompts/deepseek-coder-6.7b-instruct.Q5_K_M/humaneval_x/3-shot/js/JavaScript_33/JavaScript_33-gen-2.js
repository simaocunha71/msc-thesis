  let sorted = [...l].sort((a, b) => a - b);
  for(let i = 2; i < l.length; i += 3) {
    let temp = sorted[i];
    sorted[i] = l[i];
    l[i] = temp;
  }
  return l;
}



