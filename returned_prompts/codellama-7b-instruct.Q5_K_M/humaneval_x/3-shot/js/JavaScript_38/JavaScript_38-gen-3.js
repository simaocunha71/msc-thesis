  var groups = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (let i = 0; i < groups.length; i++) {
    if (groups[i].length == 3)
      groups[i] = groups[i][2] + groups[i].slice(0, 2);
  }
  return groups.join('');
}



