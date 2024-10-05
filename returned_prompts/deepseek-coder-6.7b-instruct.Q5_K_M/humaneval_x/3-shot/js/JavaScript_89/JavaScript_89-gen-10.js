  let result = '';
  for(let i = 0; i < s.length; i++){
    let charCode = s.charCodeAt(i);
    if(charCode >= 65 && charCode <= 90){
      result += String.fromCharCode(65 + ((charCode - 65 + 2*2) % 26));
    } else if(charCode >= 97 && charCode <= 122){
      result += String.fromCharCode(97 + ((charCode - 97 + 2*2) % 26));
    } else {
      result += s.charAt(i);
    }
  }
  return result;
}



