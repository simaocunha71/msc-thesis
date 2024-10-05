  if (arr.length === 0) {
    return true;
  }
  for (let i = 0; i < arr.length; i++) {
    let flag = true;
    for (let j = 0; j < arr.length; j++) {
      if (arr[(i + j) % arr.length] > arr[(i + j + 1) % arr.length]) {
        flag = false;
        break;
      }
    }
    if (flag) {
      return true;
    }
  }
  return false;
}



