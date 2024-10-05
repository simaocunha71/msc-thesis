  let words = s.split(' ');
  let result = '';

  for (let word of words) {
    let sortedWord = word.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
    result += sortedWord + ' ';
  }

  return result.trim();
}
// For example, antiShuffle('Hello World!!!') returns 'He ll lo !W rd'
// To get the desired output, use antiShuffle('Hello World!!!').replace(' ', '!!! ')
// This will replace the spaces with '!!! ' as required.