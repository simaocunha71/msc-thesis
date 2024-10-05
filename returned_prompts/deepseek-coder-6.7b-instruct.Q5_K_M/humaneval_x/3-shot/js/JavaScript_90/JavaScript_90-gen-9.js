  if  (lst.length < 2)  {
    return null;
  }
  
  lst.sort((a, b) => a - b);
  
  let smallest = lst[0];
  
  for  (let i = 1; i < lst.length; i++)  {
    if  (lst[i] !== smallest)  {
      return lst[i];
    }
  }
  
  return null;
}



