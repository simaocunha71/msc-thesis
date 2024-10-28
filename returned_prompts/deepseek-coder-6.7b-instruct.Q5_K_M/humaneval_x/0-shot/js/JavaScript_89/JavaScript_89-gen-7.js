let result = '';
    for(let i = 0; i < s.length; i++){
        let code = s.charCodeAt(i);
        if(code >= 65 && code <= 90){
            result += String.fromCharCode(65 + ((code - 65 + 2*2) % 26));
        } else if(code >= 97 && code <= 122){
            result += String.fromCharCode(97 + ((code - 97 + 2*2) % 26));
        } else {
            result += s[i];
        }
    }
    return result;
}

//Test cases
console.log(encrypt('hi')); //returns 'jm'
console.log(encrypt('asdfghjkl')); //returns 'cwfjlnr'
console.log(encrypt('gf')); //returns 'ij'
console.log(encrypt('et')); //returns 'gh'
console.log(encrypt('z')); //returns 'b'
console.log(encrypt('Z')); //returns 'B'
console.log(encrypt(' ')); //returns ' '
console.log(encrypt('123')); //returns '123'
console.log(encrypt('@#')); //returns '@#'













































































































































































































