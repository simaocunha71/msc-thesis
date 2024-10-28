
  var ret = Buffer.allocUnsafe(n);
  var c = 0;
  for (var i = 0, l = list.length; i < l && c < n; ++i) {
    var buf = list[i];
    var cpy = Math.min(n - c, buf.length);
    if (cpy === buf.length) {
      ret[c++] = buf[cpy - 1];
      --buf.length;
    } else {
      cpy = cpy || 0;
      var src = buf[cpy];
      var dst = ret[c++];
      dst[0] = src[0];
      --src.length;
    }
  }
  return ret;
}

// Copies a specified amount of bytes to the list of buffered data chunks.
// This function is designed to be inlinable, so please take care when making
// changes to the function body.
function copyToBuffer(buf, n, list) {
  var ret = list[list.length - 1];
  if (ret.length + n > kMaxLength) ret = Buffer.allocUnsafe(kMaxLength - ret.length);
  var c = 0;
  while (c < n) {
    var buf = list[list.length - 1];
    var cpy = Math.min(n - c, buf.length);
    if (cpy === buf.length) {
      ret[ret.length++] = buf[buf.length - 1];
      --buf.length;
    } else {
      cpy = cpy || 0;
      var src = buf[cpy];
      var dst = ret[ret.length++];
      dst[0] = src[0];
      --src.length;
    }
    c += cpy;
  }
  return ret;
}

// Copies a specified amount of bytes to the list of buffered data chunks.
// This function is designed to be inlinable, so please take care when making
// changes to the function body.
function copyToArray(buf, n, array) {
  var len = buf.length;
  if