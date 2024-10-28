  let result = '';
  const vowels = 'aeiouAEIOU';
  const alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

  for (let i = 0; i < message.length; i++) {
    if (vowels.includes(message[i])) {
      result += alphabet[(alphabet.indexOf(message[i]) + 2) % 26];
    } else {
      result += message[i] === message[i].toUpperCase() ? message[i].toLowerCase() : message[i].toUpperCase();
    }
  }

  return result;
}



