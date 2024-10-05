  if (l.length < 2) {
    return true;
  }

  let increasing = true;
  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] > l[i + 1]) {
      increasing = false;
      break;
    }
  }

  if (increasing) {
    return true;
  }

  let decreasing = true;
  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] < l[i + 1]) {
      decreasing = false;
      break;
    }
  }

  return decreasing;
}



