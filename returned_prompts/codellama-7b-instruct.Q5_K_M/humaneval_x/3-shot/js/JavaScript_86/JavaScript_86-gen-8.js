  var result = '';
  var words = s.split(' ');

  for (let word of words) {
    var chars = word.split('');
    chars.sort((a, b) => {
      return a.charCodeAt(0) - b.charCodeAt(0);
    });
    result += chars.join('');
  }

  return result;
}



