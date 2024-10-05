  var result = [];
  var temp = [];
  var temp2 = [];
  var count = 0;

  for (var i = 0; i < arr.length; i++) {
    if (arr[i] >= 1 && arr[i] <= 9) {
      temp.push(arr[i]);
    }
  }

  temp.sort(function(a, b) { return a - b; });
  temp.reverse();

  for (var i = 0; i < temp.length; i++) {
    if (temp[i] == 1) {
      temp2.push('One');
    } else if (temp[i] == 2) {
      temp2.push('Two');
    } else if (temp[i] == 3) {
      temp2.push('Three');
    } else if (temp[i] == 4) {
      temp2.push('Four');
    } else if (temp[i] == 5) {
      temp2.push('Five');
    } else if (temp[i] == 6) {
      temp2.push('Six');
    } else if (temp[i] == 7) {
      temp2.push('Seven');
    } else if (temp[i] == 8) {
      temp2.push('Eight');
    } else if (temp[i] == 9) {
      temp2.push('Nine');
    }
  }

  return temp2;
}



