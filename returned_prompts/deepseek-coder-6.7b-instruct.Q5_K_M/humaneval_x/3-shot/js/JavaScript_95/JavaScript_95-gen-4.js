  if(Object.keys(dict).length === 0){
    return false;
  }

  let allLower = true;
  let allUpper = true;

  for(let key in dict){
    if(key !== key.toLowerCase()){
      allLower = false;
    }
    if(key !== key.toUpperCase()){
      allUpper = false;
    }
  }

  return allLower || allUpper;
}



