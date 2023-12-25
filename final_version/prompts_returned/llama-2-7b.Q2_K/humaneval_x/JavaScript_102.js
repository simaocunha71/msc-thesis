/*This function takes two positive numbers x and y and returns the
  biggest even integer number that is in the range [x, y] inclusive. If 
  there's no such number, then the function should return -1.

  For example:
  chooseNum(12, 15) = 14
  chooseNum(13, 12) = -1
  */
const chooseNum = (x, y) => {
  let a = x;
  let b = y;
  
  while(!((a % 2) === 0) && !((b % 2))){
    if(x > y){
      return Math.floor(y/2);
    }else{
      return Math.ceil(x/2);
    }
    
  
  }
}
