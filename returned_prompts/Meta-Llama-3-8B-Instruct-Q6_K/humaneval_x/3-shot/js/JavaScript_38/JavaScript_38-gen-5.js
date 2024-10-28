  var result = [];
  for (const group of s.split('')) {
    if (group.length == 2) {
      result.push(group[0] + group[1]);
    } else {
      result.push(group);
    }
  }
  return result.join('');
}