  return values.filter((value) => {
    return typeof value == 'number' && Math.floor(value) == value;
  });
}



