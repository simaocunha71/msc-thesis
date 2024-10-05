  let maxStart = Math.max(interval1[0], interval2[0]);
  let minEnd = Math.min(interval1[1], interval2[1]);
  let len = minEnd - maxStart;

  if(len < 0) {
    return "NO";
  }

  if(len === 1) {
    return "NO";
  }

  for(let i = 2, sqrtLen = Math.sqrt(len); i <= sqrtLen; i++) {
    if(len % i === 0) {
      return "NO";
    }
  }

  return "YES";
}



