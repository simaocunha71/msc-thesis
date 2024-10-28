  let result = [];
  for  (let i = 0; i < n; i++)  {
    if  (i == 0)  {
      result.push(3);
    }  else if  (i == 1)  {
      result.push(1);
    }  else if  (i % 2 == 0)  {
      result.push(result[i - 1] + 1);
    }  else  {
      result.push(result[i - 1] + result[i - 2] + result[i - 3]);
    }
  }
  return result;
}



