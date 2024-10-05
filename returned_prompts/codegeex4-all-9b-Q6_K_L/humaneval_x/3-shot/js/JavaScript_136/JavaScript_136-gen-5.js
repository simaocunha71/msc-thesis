  var negative_integers = [];
  var positive_integers = [];

  for (const i of lst) {
    if (i < 0) {
      negative_integers.push(i);
    } else if (i > 0) {
      positive_integers.push(i);
    }
  }

  if (negative_integers.length > 0) {
    negative_integers.sort();
  }
  if (positive_integers.length > 0) {
    positive_integers.sort();
  }

  return [negative_integers[negative_integers.length - 1] || null,
    positive_integers[0] || null];
}



