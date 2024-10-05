  if  (strings.length  == 0)  {
    return  null;
  }

  let longestString  =  strings[0];
  for  (let i  =  1; i  <  strings.length; i++)  {
    if  (strings[i].length  > longestString.length)  {
      longestString  =  strings[i];
    }
  }

  return  longestString;
}



