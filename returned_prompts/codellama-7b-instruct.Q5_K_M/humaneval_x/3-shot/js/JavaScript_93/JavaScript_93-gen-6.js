  const message_array = Array.from(message);
  const vowels = ['a', 'e', 'i', 'o', 'u'];

  for (let i = 0; i < message_array.length; i++) {
    if (message_array[i] === message_array[i].toLowerCase()) {
      message_array[i] = message_array[i].toUpperCase();
    } else if (vowels.includes(message_array[i])) {
      const index = vowels.indexOf(message_array[i]);
      message_array[i] = vowels[index + 2];
    }
  }

  return message_array.join('');
}



