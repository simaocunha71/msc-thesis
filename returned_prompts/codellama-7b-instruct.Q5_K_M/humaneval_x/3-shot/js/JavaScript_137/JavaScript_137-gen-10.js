  if (typeof a == "string") {
    a = a.replace(",", ".");
  }
  if (typeof b == "string") {
    b = b.replace(",", ".");
  }

  if (a > b) {
    return a;
  } else if (a < b) {
    return b;
  } else {
    return null;
  }
}



