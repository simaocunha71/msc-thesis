  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor(s.length / 2); i++) {
    groups.push(s.slice(2 * i, 2 * i + 2));
  }
  for (const group of groups) {
    if (group[1] == group[0])
      groups2.push(group);
    else
      groups2.push(group.slice(1) + group[0]);
  }
  return groups2.join('');
}



