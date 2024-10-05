const decodeCyclic = (s) => {
  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      groups2.push(group[0] + group.slice(1));
    else
      groups2.push(group);
  }
  return groups2.join('');
}

/*
  takes as input string encoded with encode_cyclic function. Returns decoded string.
  */
const decodeCyclic = (s) => {
  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    groups2.push(group.split('').reverse().join(''));
  }
  return groups2.join('');
}

/*
  takes as input string encoded with encode_cyclic function. Returns decoded string.
  */
const decodeCyclic = (s) => {
  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    groups2.push(group.split('').reverse().join(''));
  }
  return groups2.join('');
}

/*
  takes as input string encoded with encode_cyclic function. Returns decoded string.
  */
const decodeCyclic = (s) => {
  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s