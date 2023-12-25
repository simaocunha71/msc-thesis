/*Given a string representing a space separated lowercase letters, return a dictionary
  of the letter with the most repetition and containing the corresponding count.
  If several letters have the same occurrence, return all of them.
  
  Example:
  histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
  histogram('a b b a') == {'a': 2, 'b': 2}
  histogram('a b c a b') == {'a': 2, 'b': 2}
  histogram('b b b b a') == {'b': 4}
  histogram('') == {}

  */
const histogram = (test) => {
  const keys = [];
  let count = 0;
  while(test.length > 0) {
    const currLen = test.length;
    if(!count && currLen){
      for(let i=0;i<currLen;i++){keys.push(test[i].toLowerCase());}
      break;
    }else{
      count++;
      if (keys.length) {
        test = test.substr(1);
        for(let j=0;j<count;j++){
          keys.forEach((k,idx)=>{test[idx] = k});
        }
        break;
      }else{
        console.log('Empty string passed');
      }
    }
  };

  return keys;
};

export default histogram;