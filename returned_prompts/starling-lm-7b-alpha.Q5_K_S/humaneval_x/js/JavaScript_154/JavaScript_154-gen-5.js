  let rotate = b => b.slice(1) + b[0];
  let bArray = [];
  bArray.push(b);
  bArray.push(rotate(b));
  bArray.push(rotate(rotate(b)));
  bArray.push(rotate(rotate(rotate(b))));

  let aArray = a.split('');
  let bArrayLength = bArray.length;
  let aArrayLength = aArray.length;
  let bArrayIndex = 0;
  let aArrayIndex = 0;
  let bArraySubstring = '';

  if (aArrayLength < bArrayLength) {
    return false;
  }

  while (aArrayIndex < aArrayLength) {
    bArraySubstring = bArray[bArrayIndex];
    if (aArray.includes(bArraySubstring)) {
      return true;
    } else {
      aArrayIndex += 1;
    }
    if (bArrayIndex == (bArrayLength - 1)) {
      bArrayIndex = 0;
    } else {
      bArrayIndex += 1;
    }
  }
  return false;
}



