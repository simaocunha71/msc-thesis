  let aSquared = Math.pow(a, 2);
  let bSquared = Math.pow(b, 2);
  let cSquared = Math.pow(c, 2);

  return (aSquared + bSquared) == cSquared || (aSquared + cSquared) == bSquared
    || (bSquared + cSquared) == aSquared;
}



