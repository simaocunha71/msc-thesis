  const value_float = parseFloat(value);
  const value_int = Math.round(value_float);

  if (value_float > 0) {
    return Math.floor(value_int + value_float % 1.0);
  } else {
    return Math.ceil(value_int - value_float % 1.0);
  }
}



