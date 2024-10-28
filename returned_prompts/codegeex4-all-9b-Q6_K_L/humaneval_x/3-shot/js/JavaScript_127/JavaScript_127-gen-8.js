  let intersection = [];
  if (interval1[0] < interval2[0]) {
    intersection.push(interval2[0]);
  } else {
    intersection.push(interval1[0]);
  }
  if (interval1[1] < interval2[1]) {
    intersection.push(interval1[1]);
  } else {
    intersection.push(interval2[1]);
  }
  let length = intersection[1] - intersection[0];
  if (length <= 1) {
    return "NO";
  } else {
    for (let i = 2; i < length; i++) {
      if (length % i == 0) {
        return "NO";
      }
    }
  }
  return "YES";
}