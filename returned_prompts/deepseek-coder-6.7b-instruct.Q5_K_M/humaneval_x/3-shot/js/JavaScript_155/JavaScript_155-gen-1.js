  let evenCount = 0;
  let oddCount = 0;
  let numStr = Math.abs(num).toString();
  for(let i=0; i<numStr.length; i++){
    if(Number(numStr[i]) % 2 === 0){
      evenCount++;
    }
    else{
      oddCount++;
    }
  }
  return [evenCount, oddCount];
}



