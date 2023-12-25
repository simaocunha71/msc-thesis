/*
  Check if two words have the same characters.
  >>> sameChars('eabcdzzzz', 'dddzzzzzzzddeddabc')
  true
  >>> sameChars('abcd', 'dddddddabc')
  true
  >>> sameChars('dddddddabc', 'abcd')
  true
  >>> sameChars('eabcd', 'dddddddabc')
  false
  >>> sameChars('abcd', 'dddddddabce')
  false
  >>> sameChars('eabcdzzzz', 'dddzzzzzzzddddabc')
  false
  */
const sameChars = (s0, s1) => {
    const n = s0.length;
    let r;
    
    for(let i=0 ; i<n ; i++){
        if(!r && s0[i] !== s1[i]){
            r = false;
        } else if (s0[i] === s1[i]) {
            r = true;
        }
    }

    return r;
}