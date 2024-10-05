  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      groups2.push(group.slice(-1) + group.slice(0, -1));
    else
      groups2.push(group);
  }
  return groups2.join('');
}

/* Test your implementation of encode_cyclic and decode_cyclic
  by applying them to a string and then decoding the result
  >>> decodeCyclic(encodeCyclic('hello world'))
  'hello world'
  */
const testEncoding = () => {
  console.log(decodeCyclic(encodeCyclic('hello world')));
}



