  let count = 0;
  for  (let i = 11; i < n; i++)  {
    if (i % 11 === 0 || i % 13 === 0)  {
      count += (i.toString().match(/7/g) || []).length;
    }
  }
  return count;
}


