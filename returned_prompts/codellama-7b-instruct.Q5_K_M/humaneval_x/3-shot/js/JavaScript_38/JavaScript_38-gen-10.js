  var groups = [];
  for (let i = 0; i < s.length; i++) {
    groups.push(s.slice(i, i + 3));
  }
  var groups2 = [];
  for (const group of groups) {
    if (group.length == 3)
      groups2.push(group[2] + group.slice(0, 2));
    else
      groups2.push(group);
  }
  return groups2.join('');
}



