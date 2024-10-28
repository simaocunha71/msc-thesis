  var i = 0;
  var c = 0;
  var ret = new Array(n);
  var chunk;
  var chunkIdx;
  var chunkLen;

  // Fast path: return the whole buffer if it's small enough.
  if (n >= list.length) {
    return list;
  }

  // Fast path: return the first chunk if it's large enough.
  if (list[0].length >= n) {
    return list[0].slice(0, n);
  }

  // Fast path: return the last chunk if it's large enough.
  if (list[list.length - 1].length >= n) {
    return list[list.length - 1].slice(n - list[list.length - 1].length);
  }

  // Fast path: return the first n bytes of the first chunk.
  ret[i++] = list[0].slice(0, n);

  // Fast path: return the last n bytes of the last chunk.
  ret[i++] = list[list.length - 1].slice(list[list.length - 1].length - n);

