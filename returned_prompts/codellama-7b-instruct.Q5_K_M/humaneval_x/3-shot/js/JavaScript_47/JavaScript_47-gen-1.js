  var sorted = l.sort();
  var len = l.length;
  if (len % 2 === 0)
    return (sorted[len / 2 - 1] + sorted[len / 2]) / 2;
  else
    return sorted[(len - 1) / 2];
}



