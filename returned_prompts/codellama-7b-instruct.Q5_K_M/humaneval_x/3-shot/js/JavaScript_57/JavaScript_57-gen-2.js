  let increasing = true;
  let decreasing = true;

  for (let i = 1; i < l.length; i++) {
    if (l[i] < l[i - 1]) {
      decreasing = false;
    }
    if (l[i] > l[i - 1]) {
      increasing = false;
    }
  }

  return increasing || decreasing;
}



