  let result = [n];
  for  (let i = 1; i < n; i++)  {
    if  (result[i-1] % 2 === 0)  {
      result.push(result[i-1] + 2);
    } else  {
      result.push(result[i-1] + 2);
    }
  }
  return result;
}



