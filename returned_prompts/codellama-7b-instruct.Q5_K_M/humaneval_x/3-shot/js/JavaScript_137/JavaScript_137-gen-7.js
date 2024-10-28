  if (typeof a == "string" && typeof b == "string") {
    a = a.replace(',', '.');
    b = b.replace(',', '.');
  }
  else if (typeof a == "string" || typeof b == "string") {
    a = parseFloat(a);
    b = parseFloat(b);
  }

  if (a > b) {
    return a;
  } else if (a < b) {
    return b;
  } else {
    return null;
  }
}



