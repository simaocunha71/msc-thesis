  let negatives = lst.filter(x => x < 0);
  let positives = lst.filter(x => x > 0);

  if (negatives.length === 0 && positives.length === 0) {
    return [null, null];
  }

  if (negatives.length === 0) {
    return [null, positives[0]];
  }

  if (positives.length === 0) {
    return [negatives[negatives.length - 1], null];
  }

  return [Math.max(...negatives), Math.min(...positives)];
}



