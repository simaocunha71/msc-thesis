  for  (let i =  1; i < lst.length; i++)  {
    if  (lst[i - 1] >= lst[i])  {
      return false;
     }
   }

  return true;
}



