  let count = 0;
  for  (let i  in brackets)  {
    if  (brackets[i] == '(')  {
      count++;
    } else if  (brackets[i] == ')')  {
      if  (count == 0)  {
        return false;
      }
      count--;
    }
  }

  return count == 0;
}



