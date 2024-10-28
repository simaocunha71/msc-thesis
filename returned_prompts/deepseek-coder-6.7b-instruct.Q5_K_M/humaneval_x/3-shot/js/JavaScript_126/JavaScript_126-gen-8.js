  for  (let i =  1; i ≤ lst.length  -  1; i++)  {
    if  (lst[i]  ≤  lst[i  -  1]  ||  lst.indexOf(lst[i])  !=  i  &&  lst.indexOf(lst[i])  ==  lst.lastIndexOf(lst[i]))  {
      return  false;
    }
  }
  return  true;
}



