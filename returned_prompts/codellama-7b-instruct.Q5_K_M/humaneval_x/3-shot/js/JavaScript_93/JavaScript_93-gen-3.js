  let result = '';
  let vowels = ['a', 'e', 'i', 'o', 'u'];

  for (let i = 0; i < message.length; i++) {
    if (vowels.includes(message[i])) {
      result += vowels[vowels.indexOf(message[i]) + 2];
    } else {
      result += message[i].toUpperCase();
    }
  }

  return result;
}



