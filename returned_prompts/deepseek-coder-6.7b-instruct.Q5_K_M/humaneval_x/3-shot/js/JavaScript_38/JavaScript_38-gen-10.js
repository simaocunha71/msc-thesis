  var groups =  [], groups2 = [];
  for  (let i  in s)  {
    groups.push(s.slice(i, i + 3));
  }
  for  (const group of groups)  {
    if  (group.length  !=  3)
      groups2.push(group);
    else
      groups2.push(group[2]  + group.slice(0, 2));
  }
  return groups2.join('');
}


