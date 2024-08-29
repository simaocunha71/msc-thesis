  let increasing = true;
  let decreasing = true;

  for (let i = 1; i < l.length; i++) {
    if (l[i] > l[i - 1]) {
      increasing = false;
    }
    if (l[i] < l[i - 1]) {
      decreasing = false;
    }
  }

  return increasing || decreasing;
}



