  let negatives = lst.filter(i => i < 0);
  let positives = lst.filter(i => i > 0);

  if (negatives.length === 0 && positives.length === 0) {
    return [null, null];
  } else if (negatives.length === 0) {
    return [null, positives[0]];
  } else if (positives.length === 0) {
    return [negatives[negatives.length - 1], null];
  } else {
    return [negatives[negatives.length - 1], positives[0]];
  }
}



