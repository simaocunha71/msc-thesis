  let count = 0;
  for  (let i = 0; i < n; i++)  {
    if  ((i % 11 === 0 || i % 13 === 0) && i.toString().includes('7'))  {
      count++;
    }
  }
  return count;
}


