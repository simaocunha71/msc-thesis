  arr.sort((a, b) => {
    return b - a;
  });

  return arr.slice(0, k);
}

