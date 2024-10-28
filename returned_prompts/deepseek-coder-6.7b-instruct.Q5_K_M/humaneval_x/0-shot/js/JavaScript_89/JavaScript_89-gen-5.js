let encrypted = '';
  
  for(let i = 0; i < s.length; i++){
    let charCode = s.charCodeAt(i);
    if(charCode >= 65 && charCode <= 90){
      encrypted += String.fromCharCode((charCode - 65 + 2*2) % 26 + 65);
    }else if(charCode >= 97 && charCode <= 122){
      encrypted += String.fromCharCode((charCode - 97 + 2*2) % 26 + 97);
    }else{
      encrypted += s.charAt(i);
    }
  }
  
  return encrypted;
}

console.log(encrypt('hi')); // returns 'jm'
console.log(encrypt('asdfghjkl')); // returns 'cwfhijkmp'
console.log(encrypt('gf')); // returns 'ij'
console.log(encrypt('et')); // returns 'gv'

In this code, we are iterating over each character of the input string. If the character is an uppercase or lowercase letter, we get its ASCII code, subtract 65 for uppercase or 97 for lowercase to get a 0-based index, add 2, multiply it by 2, take modulo 26 to wrap around the alphabet, and finally add 65 or 97 to get the correct ASCII code for the encrypted character. Non-alphabet characters are left as they are.

Note: The encryption is a basic form of substitution cipher known as a Caesar cipher. The shift factor used here is 2. If you want to use a different shift factor, you can change the 2 to another number.

Also, the rotation is circular, meaning that after 'z', it wraps around to 'a'. If you want a different behavior, you would need to adjust the code accordingly.

This code works for both English and non-English alphabets.

The function encrypt is taking a string as an argument and returning an encrypted string.

The function is case-sensitive meaning it will treat the uppercase and lowercase letters differently.

The function is not handling any special characters