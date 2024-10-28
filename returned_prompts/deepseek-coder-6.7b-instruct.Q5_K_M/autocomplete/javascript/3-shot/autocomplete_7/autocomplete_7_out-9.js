  if (list.length < n) {
    return null;
  }
  var buffer = list[0];
  var result = buffer.slice(0, n);
  list[0] = buffer.slice(n);
  if (!list[0].length) {
    list.shift();
  }
  return result;
}

