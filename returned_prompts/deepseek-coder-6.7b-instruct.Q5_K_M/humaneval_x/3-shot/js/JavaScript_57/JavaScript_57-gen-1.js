  let increasing = true;
  let decreasing = true;

  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] > l[i + 1]) {
      increasing = false;
    }
    if (l[i] < l[i + 1]) {
      decreasing = false;
    }
  }

  return increasing || decreasing;
}



