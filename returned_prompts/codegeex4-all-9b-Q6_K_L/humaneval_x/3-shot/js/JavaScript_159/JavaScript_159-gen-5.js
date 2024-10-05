  if (remaining - need <= 0) {
    return [number + remaining, 0];
  } else {
    return [number + need, remaining - need];
  }
}

