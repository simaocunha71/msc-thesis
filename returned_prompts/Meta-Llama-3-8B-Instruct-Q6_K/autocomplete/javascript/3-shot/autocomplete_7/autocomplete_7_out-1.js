  var buffer = list.buffer;
  var offset = list.offset;
  var length = list.length - offset;

  if (n > length) {
    n = length;
  }

  System.arraycopy(buffer, offset, buffer, offset + n, n);
  list.offset += n;
  list.length -= n;
}

