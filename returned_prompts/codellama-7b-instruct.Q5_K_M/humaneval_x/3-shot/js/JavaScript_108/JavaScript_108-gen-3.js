  var count = 0;

  for (var i = 0; i < arr.length; i++) {
    var sum = 0;

    for (var j = 0; j < arr[i].toString().length; j++) {
      sum += Math.abs(arr[i].toString()[j]);
    }

    if (sum > 0) {
      count += 1;
    }
  }

  return count;
}



