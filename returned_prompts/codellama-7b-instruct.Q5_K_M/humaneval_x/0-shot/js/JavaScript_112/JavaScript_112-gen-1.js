function reverseDelete(s, c) {
  let result = '';
  for (let i = 0; i < s.length; i++) {
    let isDeleted = false;
    for (let j = 0; j < c.length; j++) {
      if (s[i] === c[j]) {
        isDeleted = true;
        break;
      }
    }
    if (!isDeleted) {
      result += s[i];
    }
  }
  return {
    result,
    isPalindrome: result === result.split('').reverse().join('')
  };
}

B:
function reverseDelete(s, c) {
  const result = s.split('').filter(char => c.indexOf(char) === -1).join('');
  return {
    result,
    isPalindrome: result === result.split('').reverse().join('')
  };
}

C:
function reverseDelete(s, c) {
  return {
    result: s.split('').filter(char => c.indexOf(char) === -1).join(''),
    isPalindrome: s.split('').filter(char => c.indexOf(char) === -1).join('') === s.split('').filter(char => c.indexOf(char) === -1).join('').split('').reverse().join('')
  };
}

D:
function reverseDelete(s, c) {
  return {
    result: s.split('').filter(char => c.indexOf(char) === -1).join(''),
    isPalindrome: s.split('').filter(char => c.indexOf(char) === -1).join('') === s.split('').filter(char => c.indexOf(char) === -1).join('').split('').reverse().join('')
  };
}

E:
function reverseDelete(s, c) {
  return {
    result: s.split('').filter(char => c.indexOf(char) === -1).join(''),
    isPalindrome: s.split('').filter(char => c.indexOf(char) === -1).join('