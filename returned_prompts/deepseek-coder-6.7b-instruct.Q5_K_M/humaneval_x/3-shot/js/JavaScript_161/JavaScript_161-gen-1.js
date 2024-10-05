  let result = '';
  for(let i = 0; i < s.length; i++){
    if(s[i] === s[i].toUpperCase()){
      result += s[i].toLowerCase();
    } else if(s[i] === s[i].toLowerCase()){
      result += s[i].toUpperCase();
    } else {
      result += s[i];
    }
  }
  if(result === result.toLowerCase() || result === result.toUpperCase()){
    return result.split('').reverse().join('');
  }
  return result;
}



