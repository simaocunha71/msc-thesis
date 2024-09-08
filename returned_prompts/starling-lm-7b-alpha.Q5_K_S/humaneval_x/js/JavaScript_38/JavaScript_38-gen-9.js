  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor(s.length / 2); i++) {
    groups.push(s.slice(2 * i, Math.min((2 * i + 2), s.length)));
  }
  for (const group of groups) {
    if (group.length == 2)
      groups2.push(group[1] + group[0]);
    else
      groups2.push(group);
  }
  return groups2.join('');
}



