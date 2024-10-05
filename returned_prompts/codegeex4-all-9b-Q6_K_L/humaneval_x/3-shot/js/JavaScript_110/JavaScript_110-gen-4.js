  var count = 0;

  for (var i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 != 0) {
      count += 1;
    }
  }

  for (var j = 0; j < lst2.length; j++) {
    if (lst2[j] % 2 == 0) {
      count -= 1;
    }
  }

  if (count == 0) {
    return "YES";
  } else {
    return "NO";
  }
}