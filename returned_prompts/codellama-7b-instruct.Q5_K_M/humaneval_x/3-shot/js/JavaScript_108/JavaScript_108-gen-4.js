  var result = 0;
  var temp = 0;

  for (var i = 0; i < arr.length; i++) {
    temp = arr[i];
    while (temp > 0) {
      if (temp % 10 < 0) {
        result += 1;
        break;
      }
      temp = Math.floor(temp / 10);
    }
  }

  return result;
}



