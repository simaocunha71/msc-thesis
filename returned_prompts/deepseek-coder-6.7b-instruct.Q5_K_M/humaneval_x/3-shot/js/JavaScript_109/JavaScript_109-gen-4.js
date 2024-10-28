  if(arr.length === 0){
    return true;
  }
  for(let i = 0; i < arr.length; i++){
    let isSorted = true;
    for(let j = 0; j < arr.length - 1; j++){
      if(arr[(j + i) % arr.length] > arr[(j + 1 + i) % arr.length]){
        isSorted = false;
        break;
      }
    }
    if(isSorted){
      return true;
    }
  }
  return false;
}



