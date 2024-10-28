 // NOLINT
  var ret = '';
  var c = 0;
  while (c < n) {
    var chunk = list[list.length - 1];
    if (chunk.length <= c) {
      c -= chunk.length;
      list.pop();
      continue;
    }
    ret += chunk.substring(c);
    c += chunk.length - c;
  }
  ++c;
  list.length -= c;
  return ret;
}

// Copies a specified amount of bytes from the list of buffered data chunks.
// This function is designed to be inlinable, so please take care when making
// changes to the function body.
function copyFromBuffer(n, list) { // NOLINT
  var ret = '';
  var c = 0;
  while (c < n) {
    var chunk = list[list.length - 1];
    if (chunk.length <= c) {
      c -= chunk.length;
      list.pop();
      continue;
    }
    ret += chunk.substring(c, c + chunk.length - c);
    c += chunk.length - c;
  }
  ++c;
  list.length -= c;
  return ret;
}

// Copies a specified amount of bytes from the list of buffered data chunks.
// This function is designed to be inlinable, so please take care when making
// changes to the function body.
function copyFromBuffer(n, list) {
  var ret = '';
  var c = 0;
  while (c < n) {
    var chunk = list[list.length - 1];
    if (chunk.length <= c) {
      c -= chunk.length;
      list.pop();
      continue;
    }
    ret += chunk.substring(c, c + chunk.length - c);
    c += chunk.length - c;
  }
  list.length -= c;
  return ret;
}

// Copies a specified amount of bytes from the list of buffered data chunks.
// This function is designed to be inlinable, so please take care when making
// changes to the function body.
function copyFromBuffer(n, list) {
  var ret = '';
  var c = 0;
  while (c < n) {
    var chunk = list[list.length - 1];
    if (chunk.length <= c) {
      c -= chunk.length;
      list.pop();
      continue;
    }
    ret += chunk.substring(c, c + chunk.length - c);
    c += chunk.length - c;
  }
  return ret;
}