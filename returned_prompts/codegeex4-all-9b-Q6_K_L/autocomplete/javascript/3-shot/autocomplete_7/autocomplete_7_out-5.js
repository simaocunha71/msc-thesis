  
  if (list.length === 0) {
    return new Uint8Array(0);
  }
  let ret = new Uint8Array(n);
  let c = 0;
  while (list.length > 0 && c < n) {
    const chunk = list[0];
    const m = Math.min(chunk.length, n - c);
    ret.set(chunk.subarray(0, m), c);
    c += m;
    if (chunk.length === m) {
      list.shift();
    } else {
      chunk.copyWithin(0, m);
    }
  }
  list.length -= c;
  return ret;
}

// Appends a chunk of data to the list of buffered data chunks.
function appendBuffer(chunk, list) {
  list.push(chunk);
}

// Reads a single byte from the list of buffered data chunks.
function readByte(list) {
  if (list.length === 0) {
    return -1;
  }
  const chunk = list[0];
  const ret = chunk[0];
  if (chunk.length === 1) {
    list.shift();
  } else {
    chunk.shift();
  }
  return ret;
}

// Writes a single byte to the list of buffered data chunks.
function writeByte(byte, list) {
  if (list.length === 0) {
    list.push(new Uint8Array([byte]));
  } else {
    const chunk = list[list.length - 1];
    if (chunk.length < chunk.BYTES_PER_ELEMENT) {
      chunk.push(byte);
    } else {
      list.push(new Uint8Array([byte]));
    }
  }
}

// Reads a specified amount of bytes from the list of buffered data chunks.
function readBytes(n, list) {
  if (list.length === 0) {
    return new Uint8Array(0);
  }
  let ret = new Uint8Array(n);
  let c = 0;
  while (list.length > 0 && c < n) {
    const chunk = list[0];
    const m = Math.min(chunk.length, n - c);
    ret.set(chunk.subarray(0, m), c);
    c += m;
    if (chunk.length === m) {
      list.shift();
    } else {
      chunk.copyWithin(0, m);
    }
  }
  list.length -= c;
  return ret;
}

// Writes a specified amount of bytes to the list of buffered data chunks.
function writeBytes(bytes,