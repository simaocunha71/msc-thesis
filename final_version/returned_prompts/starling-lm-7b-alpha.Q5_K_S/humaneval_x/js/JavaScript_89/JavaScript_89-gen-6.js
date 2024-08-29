  const encrypt_letter = (l) => {
    const index = l.charCodeAt(0) - 'a'.charCodeAt(0);
    const new_index = (index + 2 * 2) % 26;
    return String.fromCharCode(new_index + 'a'.charCodeAt(0));
  };

  return s.split('').map(encrypt_letter).join('');
}



