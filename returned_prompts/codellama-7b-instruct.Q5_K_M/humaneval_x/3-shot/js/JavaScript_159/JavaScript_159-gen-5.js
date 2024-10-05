  if (number >= need) {
    return [number - need, remaining];
  } else {
    return [number, remaining - need + number];
  }
}



