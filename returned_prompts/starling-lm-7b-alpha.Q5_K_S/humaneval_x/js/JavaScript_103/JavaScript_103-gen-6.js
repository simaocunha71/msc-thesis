  if (n > m) {
    return "-1";
  }

  let total = (m - n + 1) * (n + m) / 2;
  let average = Math.round(total / (m - n + 1));
  return (average).toString(2);
}



