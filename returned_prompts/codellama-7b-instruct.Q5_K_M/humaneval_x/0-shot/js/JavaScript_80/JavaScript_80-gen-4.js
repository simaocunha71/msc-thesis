const isHappy = (s) => s.length < 3 || s.match(/(.)\1{2}/g);

B:
const isHappy = (s) => s.length < 3 || s.match(/.{3}/g).some(x => [...x].every((v, i, a) => i === a.indexOf(v)));
