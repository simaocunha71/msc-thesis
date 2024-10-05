  if (arr.length === 0) {
    return true;
  }

  var sorted = arr.sort((a, b) => { return a - b; });

  for (var i = 0; i < arr.length; i++) {
    if (arr[i] !== sorted[i]) {
      return true;
    }
  }
  return false;
}



