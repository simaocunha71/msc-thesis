  if (arr.length === 0) {
    return true;
  }

  for (let i = 0; i < arr.length; i++) {
    let flag = true;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[i]) {
        flag = false;
        break;
      }
    }
    if (!flag) {
      return false;
    }
  }
  return true;
}