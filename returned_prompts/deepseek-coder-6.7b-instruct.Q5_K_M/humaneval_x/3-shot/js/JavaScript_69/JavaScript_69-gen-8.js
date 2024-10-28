  let freq = {};
  for(let i of lst){
    if(freq[i] === undefined) freq[i] = 1;
    else freq[i] += 1;
  }
  let sortedKeys = Object.keys(freq).map(Number).sort((a, b) => b - a);
  for(let i of sortedKeys){
    if(i <= lst.length && freq[i] >= i) return i;
  }
  return -1;
}



