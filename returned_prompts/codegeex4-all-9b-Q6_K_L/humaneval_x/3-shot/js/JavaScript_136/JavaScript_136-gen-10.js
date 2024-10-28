  var negatives = [];
  var positives = [];

  for (var i = 0; i < lst.length; i++) {
    if (lst[i] < 0) {
      negatives.push(lst[i]);
    } else if (lst[i] > 0) {
      positives.push(lst[i]);
    }
  }

  if (negatives.length == 0) {
    negatives.push(null);
  }
  if (positives.length == 0) {
    positives.push(null);
  }

  negatives.sort((a, b) => b - a);
  positives.sort((a, b) => a - b);

  return [negatives[0], positives[0]];
}