  var sum = 0;
  for (let i = 0; i < k; i++) {
    let element = arr[i];
    if (element < 10) {
      sum += element;
    } else if (element < 100) {
      sum += element % 10;
    }
  }
  return sum;
}



