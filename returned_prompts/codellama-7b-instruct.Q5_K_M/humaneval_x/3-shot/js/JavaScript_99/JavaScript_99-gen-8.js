  const num = parseFloat(value);
  const floor = Math.floor(num);
  const ceil = Math.ceil(num);

  if (num - floor > ceil - num) {
    return ceil;
  } else {
    return floor;
  }
}



