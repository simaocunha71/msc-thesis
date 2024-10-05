  if(x<y){
    if(y%2==0){
      return y;
    }
    if(x%2==0){
      return x;
    }
    if(y%2===0 && x%2===0){
      return y;
    }
    if(y%2!==0 && x%2!==0){
      return -1;
    }
    if(y%2!==0 && x%2===0){
      return x;
    }
    if(y%2===0 && x%2!==0){
      return y;
    }
  }
  if(x>y){
    if(x%2==0){
      return x;
    }
    if(y%2==0){
      return y;
    }
    if(y%2===0 && x%2===0){
      return x;
    }
    if(y%2!==0 && x%2!==0){
      return -1;
    }
    if(y%2!==0 && x%2===0){
      return x;
    }
    if(y%2===0 && x%2!==0){
      return y;
    }
  }
};

console.log(chooseNum(12, 15));
console.log(chooseNum(13, 12));







*/












































































































































































