  let num = parseFloat(value);
  let floorNum = Math.floor(num);
  let ceilNum = Math.ceil(num);
  let roundedNum = Math.round(num);

  if (Math.abs(num - floorNum) < Math.abs(ceilNum - num)) {
    return num > 0 ? floorNum : ceilNum;
  } else if (Math.abs(num - floorNum) > Math.abs(ceilNum - num)) {
    return num > 0 ? ceilNum : floorNum;
  } else {
    return roundedNum;
  }
}



