  if (xs.length % 2 == 0 && xs[0] != 0) {
    let x = -xs[1] / xs[0];
    return x;
  } else {
    throw new Error("Invalid polynomial");
  }
}