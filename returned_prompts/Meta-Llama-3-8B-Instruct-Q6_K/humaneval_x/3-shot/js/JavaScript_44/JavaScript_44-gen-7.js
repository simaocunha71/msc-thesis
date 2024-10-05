  let result = '';
  while (x > 0) {
    x = parseInt(x.toString().split('.')[0], 10);
    result = (x % base).toString() + result;
    x = parseInt(x.toString().split('.')[1], 10) / base | 0;
  }
  return result;
}