  for (let i = 0; i < arr.length; i++) {
    let flag = true;
    for (let j = 0; j < arr.length - 1; j++) {
      if (arr[(j + i) % arr.length] > arr[(j + 1 + i) % arr.length]) {
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



