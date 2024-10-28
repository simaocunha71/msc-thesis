  let increasing = true;
  let decreasing = true;

  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] < l[i + 1]) {
      decreasing = false;
    } else if (l[i] > l[i + 1]) {
      increasing = false;
    }
  }

  return increasing || decreasing;
}



