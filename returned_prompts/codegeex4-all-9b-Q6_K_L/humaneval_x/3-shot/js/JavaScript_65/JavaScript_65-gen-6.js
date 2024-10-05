  x = x.toString();
  let arr = x.split('');
  if (shift > arr.length) {
    arr.reverse();
    return arr.join('');
  } else {
    return arr.slice(-shift).concat(arr.slice(0, -shift)).join('');
  }
}



