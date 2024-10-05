const encrypt = (s) => {
  const shift = 2 * 2;
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let encrypted = '';
  for (let i = 0; i < s.length; i++) {
    const char = s.charAt(i);
    const index = alphabet.indexOf(char);
    if (index > -1) {
      encrypted += alphabet.charAt((index + shift) % 26);
    }
  }
  return encrypted;
}

