  let result = '';
  for(let i = 0; i < s.length; i++){
    if(s[i].match(/[a-z]/i)){
      result += s[i] === s[i].toUpperCase() ? s[i].toLowerCase() : s[i].toUpperCase();
    } else {
      result += s[i];
    }
  }
  return s.match(/[a-z]/i) ? result : s.split('').reverse().join('');
}



