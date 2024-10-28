  let words = s.split(' ');
  let result = '';

  for (let i = 0; i < words.length; i++) {
    let word_chars = words[i].split('');
    word_chars.sort((a, b) => {
      return a.charCodeAt(0) - b.charCodeAt(0);
    });
    result += word_chars.join('');
    result += ' ';
  }

  return result.trim();
}



