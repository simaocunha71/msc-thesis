  if  (Object.keys(dict).length  == 0) {
    return false;
  }

  let lower = 0;
  let upper = 0;

  for  (let key in dict)  {
    if  (key  == key.toLowerCase()) {
      lower += 1;
    } 
    if  (key  == key.toUpperCase()) {
      upper += 1;
    }
  }

  return  (lower  == Object.keys(dict).length)  || (upper  == Object.keys(dict).length);
}


