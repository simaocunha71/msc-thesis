const reverseDelete = (s, c) => {
  let res = s.split('').filter(x => c.indexOf(x) === -1).join('');
  return [res, res === res.split('').reverse().join('')];
}

B:
const reverseDelete = (s, c) => {
  let res = s.split('').filter(x => !c.includes(x)).join('');
  return [res, res === res.split('').reverse().join('')];
}

C:
const reverseDelete = (s, c) => {
  let res = s.split('').filter(x => c.indexOf(x) === -1).join('');
  return [res, res.split('').reverse().join('') === res];
}

D:
const reverseDelete = (s, c) => {
  let res = s.split('').filter(x => c.indexOf(x) === -1).join('');
  return [res, res === res.split('').reverse().join('')];
}
