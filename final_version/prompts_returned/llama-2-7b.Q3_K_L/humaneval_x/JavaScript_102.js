/*This function takes two positive numbers x and y and returns the
  biggest even integer number that is in the range [x, y] inclusive. If 
  there's no such number, then the function should return -1.

  For example:
  chooseNum(12, 15) = 14
  chooseNum(13, 12) = -1
  */
const chooseNum = (x, y) => {
  let currentEvenNumber = 0;
  let result;
    while(currentEvenNumber <= x && currentEvenNumber < y){
      console.log(`while: ${currentEvenNumber}`)
      if(currentEvenNumber % 2 === 0) {
        result = currentEvenNumber;
      } else {
        result = -1;
        break;
      }
    }
    return result;
};
console.log(`chooseNum: ${chooseNum(1, 9)}`)