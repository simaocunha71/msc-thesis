  if (l.length <= 1) {
    return true;
  }

  let increasing = true;
  for (let i = 1; i < l.length; i++) {
    if (l[i] < l[i - 1]) {
      increasing = false;
    }
  }
  return increasing;
}



