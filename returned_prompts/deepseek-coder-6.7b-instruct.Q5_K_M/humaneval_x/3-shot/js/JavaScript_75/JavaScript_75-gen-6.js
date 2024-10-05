  if(a < 100){
    let count = 0;
    for(let i = 2; i <= a; i++){
      if(a % i === 0){
        while(a % i === 0){
          a = a / i;
          count++;
        }
      }
    }
    if(count === 3){
      return true;
    }
    return false;
  }
}



