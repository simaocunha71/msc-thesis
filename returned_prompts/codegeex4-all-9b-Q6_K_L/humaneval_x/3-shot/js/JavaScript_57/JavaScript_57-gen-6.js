  if (l.every((x) => x <= l[0])) {
    return true;
  } else if (l.every((x) => x >= l[0])) {
    return true;
  } else {
    return false;
  }
}



