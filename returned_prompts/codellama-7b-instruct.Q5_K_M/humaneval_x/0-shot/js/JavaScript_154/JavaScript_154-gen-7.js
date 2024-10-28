/*You are given 2 words. You need to return true if the second word or any of its rotations is a substring in the first word*/
const cycpatternCheck = (a, b) => {

  let cycArr = [];
  let subString = '';
  let result = false;

  for(let i = 0; i < b.length; i++){
    cycArr.push(b.substring(i));
  }

  for(let i = 0; i < a.length; i++){
    for(let j = 0; j < cycArr.length; j++){
      subString = cycArr[j];
      if(a.includes(subString)){
        result = true;
        break;
      }
    }
    if(result === true){
      break;
    }
  }
  return result;
}

/*

*/



