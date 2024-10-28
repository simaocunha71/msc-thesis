  var result = 0;
  var mirror = arr.slice();
  mirror = mirror.reverse();

  for (var i = 0; i < arr.length; i++) {
    if (arr[i] != mirror[i]) {
      result += 1;
    }
  }

  return result;
}



