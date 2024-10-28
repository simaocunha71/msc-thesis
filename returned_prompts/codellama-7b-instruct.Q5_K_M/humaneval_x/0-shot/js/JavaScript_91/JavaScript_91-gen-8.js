const isBored = (S) => {
  let boredoms = 0;
  const sentences = S.split('.').join('').split('?').join('').split('!').join('');
  sentences.forEach(sentence => {
    if (sentence.startsWith('I')) {
      boredoms += 1;
    }
  });
  return boredoms;
}

// B
const isBored = (S) => {
  let boredoms = 0;
  S.split('.')
    .join('')
    .split('?')
    .join('')
    .split('!')
    .join('')
    .split(' ')
    .forEach(word => {
      if (word === 'I') {
        boredoms++;
      }
    });
  return boredoms;
};

// C
const isBored = (S) => {
  let boredoms = 0;
  S.split('.')
    .join('')
    .split('?')
    .join('')
    .split('!')
    .join('')
    .split(' ')
    .forEach(word => {
      if (word.startsWith('I')) {
        boredoms++;
      }
    });
  return boredoms;
};

// D
const isBored = (S) => {
  let boredoms = 0;
  S.split('.')
    .join('')
    .split('?')
    .join('')
    .split('!')
    .join('')
    .split(' ')
    .forEach(word => {
      if (word.includes('I')) {
        boredoms++;
      }
    });
  return boredoms;
};
