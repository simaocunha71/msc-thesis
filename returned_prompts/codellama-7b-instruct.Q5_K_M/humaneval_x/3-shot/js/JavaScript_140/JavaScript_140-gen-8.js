  let newText = '';
  let spaceCount = 0;
  let consecutiveSpaces = 0;

  for (let i = 0; i < text.length; i++) {
    let char = text[i];

    if (char === ' ') {
      spaceCount++;
    }

    if (spaceCount === 0 || spaceCount % 2 !== 0) {
      newText += char;
    } else if (spaceCount % 2 === 0) {
      consecutiveSpaces++;
      if (consecutiveSpaces === 2) {
        newText += '-';
        consecutiveSpaces = 0;
      }
    }
  }

  return newText.replace(/_/g, ' ');
}



