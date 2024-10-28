let count = 0;
const vowels = ['a', 'e', 'i', 'o', 'u'];

for (let i = 0; i < s.length; i++) {
  if (vowels.includes(s[i])) {
    count++;
  }
}

if (s[s.length-1] === 'y') {
  count++;
}

return count;
}
*/

/*
