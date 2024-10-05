  var result = [];
  var groups = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      result.push(group[2] + group.slice(1));
    else
      result.push(group);
  }
  return result.join('');
}



