  if  (Object.keys(dict).length  == 0)  {
    return false;
  }
  
  let lower =  true;
  let upper  true;
  
  for  (let key in dict)  {
    if  (key  ==  key.toLowerCase())  {
      upper  =  false;
    } else if  (key  ==  key.toUpperCase())  {
      lower  =  false;
    } else  {
      return false;
    }
  }
  
  return lower  or  upper;
}



