  if (arr.length === 0) {
    return true;
  }
  for (let i = 0; i < arr.length; i++) {
    let flag = true;
    for (let j = 0; j < arr.length - 1; j++) {
      if (arr[j] > arr[(j+1)%arr.length]) {
        flag = false;
        break;
      }
    }
    if (flag) {
      return true;
    }
    arr.unshift(arr.pop());
  }
  return false;
}



