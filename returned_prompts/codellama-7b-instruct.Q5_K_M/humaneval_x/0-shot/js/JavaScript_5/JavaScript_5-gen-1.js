
const intersperse = (numbers, delimeter) => numbers.reduce((acc, curr, i) => (i !== 0 && acc.push(delimeter), acc.push(curr)), []);

