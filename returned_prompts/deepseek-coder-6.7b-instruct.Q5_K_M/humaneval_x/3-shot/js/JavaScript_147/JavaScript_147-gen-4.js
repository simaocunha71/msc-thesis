  let arr = new Array(n).fill(0).map((_, i) => (i+1)**2 - i);
  let count = 0;
  for(let i = 0; i < n; i++)
    for(let j = i+1; j < n; j++)
      for(let k = j+1; k < n; k++)
        if((arr[i] + arr[j] + arr[k]) % 3 === 0)
          count++;
  return count;
}



