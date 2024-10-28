  let result = '';
  for(let i = 0; i < s.length; i++){
    let charCode = s.charCodeAt(i);
    if((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122)){
      result += String.fromCharCode(charCode + 2 * 2);
    } else {
      result += s.charAt(i);
    }
  }
  return result;
}



