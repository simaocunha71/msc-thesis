  let count = 0;

  for  (let i = 0; i < string.length; i++)  {
    if  (string[i] === '[')  {
      count++;
    }  else  {
      if  (count === 0)  {
        return false;
      }
      count--;
    }
  }

  return count === 0;
}



