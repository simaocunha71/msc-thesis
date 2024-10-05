  var result = [];
  var count = 0;
  for (const c2 of s) {
    if (!c.includes(c2)) {
      result.push(c2);
    }
  }
  if (result.join('') == result.reverse().join('')) {
    return [result.join(''), true];
  } else {
    return [result.join(''), false];
  }
}



