  return values.filter(value => {
    return typeof value === 'number' && value === Math.floor(value);
  });
}



