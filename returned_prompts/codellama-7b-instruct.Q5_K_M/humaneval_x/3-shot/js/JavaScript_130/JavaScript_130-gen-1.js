  var result = [];
  var tri_1 = 1;
  var tri_2 = 1;
  var tri_3 = 3;
  result.push(1);
  result.push(3);
  result.push(2);

  if (n == 3) {
    return result;
  }

  while (result.length <= n + 1) {
    var temp = tri_1 + tri_2 + tri_3;
    result.push(temp);
    tri_1 = tri_2;
    tri_2 = tri_3;
    tri_3 = temp;
  }

  return result;
}



