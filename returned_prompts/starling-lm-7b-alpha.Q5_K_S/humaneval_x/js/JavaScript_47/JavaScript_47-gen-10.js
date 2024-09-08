  l.sort(function(a,b) {return a-b;});
  let mid = Math.floor(l.length / 2);
  if (l.length % 2 == 0) {
    return (l[mid] + l[mid - 1]) / 2;
  } else {
    return l[mid];
  }
}



