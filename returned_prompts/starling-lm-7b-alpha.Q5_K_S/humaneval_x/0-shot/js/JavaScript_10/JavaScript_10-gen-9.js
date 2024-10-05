  let palindromePrefix = string.split('').reverse().join('');
  while (palindromePrefix.length > 0 && palindromePrefix.length < string.length && string.substring(0, palindromePrefix.length) === palindromePrefix) {
    palindromePrefix = string.split('').reverse().join('');
  }

  return `${string.substring(0, palindromePrefix.length)}${palindromePrefix.split('').reverse().join('')}${string.substring(palindromePrefix.length)}`;
}

/*
  Finds a center of the given string.
  If the string is odd-length, returns the center character.
  If the string is even-length, returns a substring with the two center characters.
  >>> centerString('')
  ''
  >>> centerString('cat')
  ''
  >>> centerString('cata')
  'a'
  >>> centerString('banana')
  'anan'
  */
const centerString = (string) => {
  return string.length % 2 === 0 ? string.substring(string.length / 2 - 1, string.length / 2 + 1) : string.charAt(string.length / 2);
}

/*
  Generates all permutations of the string.
  >>> permutations('cat')
  [ 'cat', 'cta', 'ct', 'ata', 'ac', 'a' ]
  */
const permutations = (string) => {
  let result = [];
  if (string.length <= 2) {
    return [string];
  }
  for (let i = 0; i < string.length; i++) {
    let current = string[i];
    let remaining = string.substring(0, i) + string.substring(i + 1);
    let perms = permutations(remaining);
    for (let j = 0; j < perms.length; j++) {
      result.push(current + perms[j]);
    }
  }
  return result;
}

/*
  Generates all unique permutations of the string.
  >>>