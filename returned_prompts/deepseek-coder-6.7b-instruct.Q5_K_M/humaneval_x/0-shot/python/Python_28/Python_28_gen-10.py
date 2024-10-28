  let num = parseFloat(value);
  let floorNum = Math.floor(num);
  let ceilNum = Math.ceil(num);

  if (num - floorNum < ceilNum - num) {
    return floorNum;
  } else if (num - floorNum > ceilNum - num) {
    return ceilNum;
  } else {
    return num > 0 ? ceilNum : floorNum;
  }
}



