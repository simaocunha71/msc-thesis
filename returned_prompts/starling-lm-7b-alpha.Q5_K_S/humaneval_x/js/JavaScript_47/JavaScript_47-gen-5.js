  l.sort(function(a,b){return a-b});
  let len = l.length;
  if (len % 2 === 1) {
    return l[Math.floor(len / 2)];
  } else {
    return (l[len / 2 - 1] + l[len / 2]) / 2.0;
  }
}


