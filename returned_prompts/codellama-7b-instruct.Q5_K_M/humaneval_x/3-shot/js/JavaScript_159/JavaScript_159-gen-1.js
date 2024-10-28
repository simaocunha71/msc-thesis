  let result = [number, remaining];

  if (need > remaining) {
    result[0] = number + remaining;
    result[1] = 0;
  }

  return result;
}



