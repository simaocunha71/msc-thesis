  return xs.map((_, i, arr) => i > 0 ? arr[i] * i : 0).filter((_, i) => i > 0);
}



