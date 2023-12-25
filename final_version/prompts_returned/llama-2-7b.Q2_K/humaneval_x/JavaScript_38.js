/*
  returns encoded string by cycling groups of three characters.
  */
const encodeCyclic = (s) => {
  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      groups2.push(group.slice(1) + group[0]);
    else
      groups2.push(group);
  }
  return groups2.join('');
}

/*
  takes as input string encoded with encode_cyclic function. Returns decoded string.
  */
const decodeCyclic = (s) => {
  var sgroups = [], sgroups2 = [];
  for (let i = -1; i < Math.floor((s.length + 2) / 3); i++) {
    sgroups.push(s.slice(i * 3, i * 3 + 3));
  }
  for (const group of sgroups) {
    if (group.length == 3 && !/^[A-Z]$/.test(s))
      sgroups2.push(decodeURIComponent(group[0]));
    else if (!/(^[A-Z]+$)/gm.test(group))
      sgroups2.push(encodeURIComponent(group));
    else
      sgroups2.push(group);
  }
  return sgroups2.join('');
}

/*
  takes a string and returns all the encoded strings that can be formed from it.
*/
const encodeCyclicAll = (s) => {
  const groupsBy3s = [];
  for (let i = -1; i < Math.floor((s.length + 2) / 3); i++) {
    if (!/(^[A-Z]*$)/gm.test(s)) {
      groupsBy3s.push(decodeURIComponent(groupsBy3s[i]));
    } else {
     