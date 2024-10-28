  function antiShuffle(str){
  let words = str.split(' ');
  let newStr = '';
  for(let i=0; i<words.length; i++){
    let char = words[i].split('');
    char.sort();
    newStr += char.join('');
    if(i<words.length-1) newStr += ' ';
  }
  return newStr;
}

