  var result = 0;

  for (let i = 0; i < k; i++) {
    let n = arr[i];
    if (n < 100) {
      result += n;
    }
  }

  return result;
}



