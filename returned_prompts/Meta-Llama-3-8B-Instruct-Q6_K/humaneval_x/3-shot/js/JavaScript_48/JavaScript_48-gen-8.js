  let cleanText = text.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  return cleanText === cleanText.split('').reverse().join('');
}