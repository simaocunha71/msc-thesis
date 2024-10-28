  var i, j, chunk, chunkLength, length;

  if (!list || !list.length) {
    return '';
  }

  length = Math.min(n, list.length);
  i = j = 0;
  chunk = list[0];
  chunkLength = chunk.length;

  while (length > 0) {
    if (chunkLength > length) {
      chunkLength = length;
    }

    n -= chunkLength;
    length -= chunkLength;

    ret = ret.concat(chunk.substring(i, i + chunkLength));

    i += chunkLength;
    if (i >= chunkLength) {
      i = 0;
      j++;
      chunk = list[j];
      chunkLength = chunk.length;
    }
  }
}