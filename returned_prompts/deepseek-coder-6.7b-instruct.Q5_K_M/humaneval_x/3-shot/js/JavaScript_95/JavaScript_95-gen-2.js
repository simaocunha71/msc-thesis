  if  (Object.keys(dict).length  == 0)  {
    return false;
  }

  let allLowerCase  = true;
  let allUpperCase  = true;

  for  (let key in dict)  {
    if  (key  !=  key.toLowerCase())  {
      allLowerCase  =  false;
    }
    if  (key  !=  key.toUpperCase())  {
      allUpperCase  =  false;
    }
  }

  return  allLowerCase  ||  allUpperCase;
}



