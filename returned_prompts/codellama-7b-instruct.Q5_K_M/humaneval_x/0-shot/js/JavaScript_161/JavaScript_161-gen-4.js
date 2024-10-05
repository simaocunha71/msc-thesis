/*
  return s.split('').map(c => c.match(/[a-z]/i) ? c.toUpperCase() : c.toLowerCase()).join('');

*/

B:
/*
  let result = '';
  for(let i = 0; i < s.length; i++) {
    result += s[i].match(/[a-z]/i) ? s[i].toUpperCase() : s[i].toLowerCase();
  }
  return result;
*/

C:
/*
  let result = '';
  for(let i = 0; i < s.length; i++) {
    if(s[i].match(/[a-z]/i)) {
      result += s[i].toUpperCase();
    } else {
      result += s[i];
    }
  }
  return result;
*/

D:
/*
  let result = '';
  for(let i = 0; i < s.length; i++) {
    if(s[i].match(/[a-z]/i)) {
      result += s[i].toUpperCase();
    } else {
      result += s[i];
    }
  }
  return result;
*/

E:
/*
  let result = '';
  for(let i = 0; i < s.length; i++) {
    if(s[i].match(/[a-z]/i)) {
      result += s[i].toUpperCase();
    } else {
      result += s[i];
    }
  }
  return result;
*/

F:
/*
  let result = '';
  for(let i = 0; i < s.length; i++) {
    if(s[i].match(/[a-z]/i)) {
      result += s[i].toUpperCase();
    } else {
      result += s[i];
    }
  }
  return result;
*/

G:
/*
  let result = '';
  for(let i = 0; i < s.length; i++) {
    if(s[i].match(/[a-