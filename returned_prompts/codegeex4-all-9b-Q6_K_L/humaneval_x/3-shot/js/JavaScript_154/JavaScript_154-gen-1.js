  var bLength = b.length;
  var aLength = a.length;
  var bRotations = [];
  var i, j;

  for (i = 0; i < bLength; i++) {
    var rotation = b.substr(i) + b.substr(0, i);
    bRotations.push(rotation);
  }

  for (i = 0; i < bRotations.length; i++) {
    var rotation = bRotations[i];
    for (j = 0; j <= aLength - bLength; j++) {
      var substring = a.substr(j, bLength);
      if (rotation === substring) {
        return true;
      }
    }
  }

  return false;
}



