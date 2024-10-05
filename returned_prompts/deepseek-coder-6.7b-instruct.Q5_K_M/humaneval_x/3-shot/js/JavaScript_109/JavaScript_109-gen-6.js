  for  (let  i =0; i < arr.length; i++) {
    let  is_sorted = true;
    for  (let  j =0; j < arr.length - i - 1; j++) {
      if  (arr[j] > arr[j + 1]) {
        is_sorted = false;
       break;
      }
    }
    if  (is_sorted) {
      return true;
    }
    arr.unshift(arr.pop());
  }
  return false;
}



