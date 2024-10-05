  s = s.toLowerCase();
  let vowels = ['a', 'e', 'i', 'o', 'u'];
  let count = 0;

  for(let letter of s) {
    if(vowels.includes(letter)) {
      count += 1;
    }
  }

  // check for 'y' at the end of the string
  if(s[s.length - 1] === 'y') {
    count += 1;
  }

  return count;
}
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
