  const vowels = {'a':'c', 'e':'g', 'i':'k', 'o':'m', 'u':'q', 'A':'C', 'E':'G', 'I':'K', 'O':'M', 'U':'Q'};
  let result = '';
  for (let i = 0; i < message.length; i++){
    if (message[i] in vowels){
      result += vowels[message[i]];
    } else if (message[i] === message[i].toUpperCase()){
      result += message[i].toLowerCase();
    } else {
      result += message[i].toUpperCase();
    }
  }
  return result;
}



