  const bLen = b.length;
  if(a.length < bLen) return false;
  for(let i = 0; i < bLen; i++) {
    const pattern = b.slice(i) + b.slice(0, i);
    if(a.includes(pattern)) return true;
  }
  return false;
}



