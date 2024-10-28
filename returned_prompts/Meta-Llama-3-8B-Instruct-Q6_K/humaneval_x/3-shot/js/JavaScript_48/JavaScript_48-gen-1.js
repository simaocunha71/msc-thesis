  var clean_text = text.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  var reversed_text = clean_text.split('').reverse().join('');
  return clean_text == reversed_text;
}.



