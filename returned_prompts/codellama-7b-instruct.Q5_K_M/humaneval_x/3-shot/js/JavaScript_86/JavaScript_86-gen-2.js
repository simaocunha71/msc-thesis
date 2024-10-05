  var words = s.split(' ');
  var result = '';

  for (var i = 0; i < words.length; i++) {
    var letters = words[i].split('');
    letters.sort();
    result += letters.join('');

    if (i != words.length - 1) {
      result += ' ';
    }
  }

  return result;
}



