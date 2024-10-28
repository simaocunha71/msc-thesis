const antiShuffle = (s) => {
  let words = s.split(' ');
  let newStr = '';
  for (let i = 0; i < words.length; i++) {
    let charArr = words[i].split('');
    charArr.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0));
    newStr += charArr.join('');
  }
  return newStr;
}
