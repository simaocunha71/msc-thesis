  let intersectionStart = Math.max(interval1[0], interval2[0]);
  let intersectionEnd = Math.min(interval1[1], interval2[1]);
  let intersectionLength = intersectionEnd - intersectionStart;

  if (intersectionLength < 0) {
    return "NO";
  } else {
    if (intersectionLength == 1 || intersectionLength == 2) {
      return "YES";
    } else if (intersectionLength % 2 == 0) {
      return "NO";
    } else {
      for (let i = 3; i <= Math.sqrt(intersectionLength); i += 2) {
        if (intersectionLength % i == 0) {
          return "NO";
        }
      }
      return "YES";
    }
  }
}