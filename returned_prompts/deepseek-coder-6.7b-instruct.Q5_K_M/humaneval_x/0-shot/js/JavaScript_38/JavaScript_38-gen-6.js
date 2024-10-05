/*
  takes as input string encoded with encode_cyclic function. Returns decoded string.
  */
const decodeCyclic 
= (s) => {
  var groups = [], groups2 = [];
  for 
  (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for 
  (const group of groups) {
    if 
    (group.length == 3)
      groups2.push(group[group.length - 1] + group.slice(0, group.length - 1));
    else
      groups2.push(group);
  }
  return groups2.join('');
}

const s = 'Hello, World';
const encoded = encodeCyclic(s);
console.log(encoded);
const decoded = decodeCyclic(encoded);
console.log(decoded);

// Output:
// elHlo,Wrd
// Hello, World

Q2:
const alphabet = 'abcdefghijklmnopqrstuvwxyz';
const encodeShift = (s) => {
  let encoded = '';
  for (const char of s) {
    if (alphabet.includes(char.toLowerCase())) {
      const charIndex = alphabet.indexOf(char.toLowerCase());
      const newIndex = (charIndex + 1) % 26;
      const newChar = alphabet[newIndex];
      encoded += char === char.toLowerCase() ? newChar : newChar.toUpperCase();
    } else {
      encoded += char;
    }
  }
  return encoded;
}

const decodeShift = (s) => {
  let decoded = '';
  for (const char of s) {
    if (alphabet.includes(char.toLowerCase())) {
      const charIndex = alphabet.indexOf(char.toLowerCase());
      const newIndex = (charIndex - 1 + 26) % 26;
      const