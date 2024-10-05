  if(Object.keys(dict).length === 0){
    return false;
  }

  let isAllLowerCase = true;
  let isAllUpperCase = true;

  for(let key in dict){
    if(key !== key.toLowerCase()){
      isAllLowerCase = false;
    }
    if(key !== key.toUpperCase()){
      isAllUpperCase = false;
    }
  }

  return isAllLowerCase || isAllUpperCase;
}



