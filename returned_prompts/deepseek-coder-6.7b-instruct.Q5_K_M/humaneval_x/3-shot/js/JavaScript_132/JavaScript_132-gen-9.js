  let count = 0;
  for  (let i = 0; i < string.length; i++)  {
    if (string[i] == '[')  {
      count++;
    }  else  {
      count--;
    }
    if (count < 0)  {
      return false;
    }
  }
  return count > 0;
}



