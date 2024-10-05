  return lst.sort((a, b) => b - a).find((n, i) => n >= i + 1) || -1;
}
