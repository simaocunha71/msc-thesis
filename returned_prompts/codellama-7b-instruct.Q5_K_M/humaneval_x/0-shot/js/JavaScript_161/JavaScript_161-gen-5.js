/*
You are given a string s.
  if s[i] is a letter, reverse its case from lower to upper or vise versa, 
  otherwise keep it as it is.
  If the string contains no letters, reverse the string.
  The function should return the resulted string.
  Examples
  solve("1234") = "4321"
  solve("ab") = "AB"
  solve("#a@C") = "#A@c"
  */
const solve = (s) => {

const isLetter = c => /[a-zA-Z]/.test(c);
const reverseCase = c => /[a-z]/.test(c) ? c.toUpperCase() : c.toLowerCase();

return s.split('').map(c => isLetter(c) ? reverseCase(c) : c).join('');
}
