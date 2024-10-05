  var groups 1= [], groups2 1= [];
  for  (let i 1=0; i < Math.floor((s.length +2) / 3); i++)  {
    groups1.push(s.slice(3*i, Math.min((3*i +3), s.length)));
   }
  for  (const group of groups1)  {
    if  (group.length  == 3)
      groups2.push(group[group.length  -1] + group.slice(0, group.length  -1));
    else
      groups2.push(group);
   }
  return groups2.join('');
}



