  var l3 = [];
  var l_not3 = [];

  for (let i = 0; i < l.length; i++) {
    if (i % 3 == 2) {
      l3.push(l[i]);
    } else {
      l_not3.push(l[i]);
    }
  }

  l3.sort();

  for (let i = 0; i < l3.length; i++) {
    l_not3.push(l3[i]);
  }

  return l_not3;
}



