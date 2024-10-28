  let count = 0;
  const n = arr.length;
  for(let i = 0; i < Math.floor(n/2); i++) {
    if(arr[i] !== arr[n-1-i]) count++;
  }
  return count;
}



