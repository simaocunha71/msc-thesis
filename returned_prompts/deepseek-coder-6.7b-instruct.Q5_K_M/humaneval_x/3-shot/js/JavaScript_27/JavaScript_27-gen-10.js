  return string.split('').map(character => {
    return character === character.toLowerCase()
      ? character.toUpperCase()
      : character.toLowerCase();
  }).join('');
}



