const encrypt = (str) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const newAlphabet = alphabet.slice(2) + alphabet.slice(0, 2);
  const newStr = str.split('').map((c) => newAlphabet[alphabet.indexOf(c)]).join('');
  return newStr;
}

B:
const encrypt = (str) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const shift = 2 * 2;
  const newAlphabet = alphabet.slice(shift) + alphabet.slice(0, shift);
  const newStr = str.split('').map((c) => newAlphabet[alphabet.indexOf(c)]).join('');
  return newStr;
}

C:
const encrypt = (str) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const shift = 2 * 2;
  const newAlphabet = alphabet.split('').map((c, i) => (i >= shift ? c : alphabet[i + shift])).join('');
  const newStr = str.split('').map((c) => newAlphabet[alphabet.indexOf(c)]).join('');
  return newStr;
}

D:
const encrypt = (str) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const shift = 2 * 2;
  const newAlphabet = alphabet.split('').map((c, i) => (i >= shift ? c : alphabet[i + shift])).join('');
  const newStr = str.split('').map((c) => newAlphabet[alphabet.indexOf(c)]).join('');
  return newStr;
}

E:
const encrypt = (str) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const shift = 2 * 2;
  const newAlphabet = alphabet.split('').map((c, i) => (i >= shift ? c : alphabet[i + shift])).join('