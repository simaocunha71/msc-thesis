  const n = Number(value);
  let result;
  if (n === Math.floor(n)) {
    result = n;
  } else if (n > 0) {
    result = Math.ceil(n);
  } else {
    result = Math.floor(n);
  }
  return result;
}



