  if (n <= 0) return;
  var ret, c;
  ret = new Buffer(n);
  c = 0;
  for (var i = 0; i < list.length && c < n; i++) {
    var buffer = list[i];
    var len = buffer.length;
    if (len > n - c) len = n - c;
    buffer.copy(ret, c, 0, len);
    c += len;
  }
  return ret;
}

