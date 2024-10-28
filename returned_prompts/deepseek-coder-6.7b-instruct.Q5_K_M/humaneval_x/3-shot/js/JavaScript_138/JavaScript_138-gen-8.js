  let count = 0;
  for(let i = 2; i < n; i += 2) {
    if(i % 2 === 0) {
      count += i;
    }
    if(count === n) {
      return true;
    }
  }
  return false;
}



