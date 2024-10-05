  let result = [];
  
  for(let i = 0; i < x.length; i++){
    let num = x[i].toString();
    let flag = false;
    for(let j = 0; j < num.length; j++){
      if(num[j] % 2 == 0){
        flag = true;
        break;
      }
    }
    if(!flag){
      result.push(parseInt(num));
    }
  }
  
  result.sort((a, b) => a - b);
  return result;
}



