  let result = "";
  for(let i = 0; i < string.length; i++) {
    if(string[i] >= 'a' && string[i] <= 'z') {
      result += String.fromCharCode(string.charCodeAt(i) - 32);
    } else {
      result += String.fromCharCode(string.charCodeAt(i) + 32);
    }
  }

  return result;
}



