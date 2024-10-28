  let str = x.toString();
  let len = str.length;

  if (shift >= len) {
    return str.split('').reverse().join('');
  }

  let front = str.substring(0, len - shift);
  let back = str.substring(len - shift, len);

  return back + front;
}



