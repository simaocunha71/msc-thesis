```javascript
const parseMusic = (music_string) => {
  return music_string.split(' ').map(n => {
    switch (n) {
      case 'o':
        return 4;
      case 'o|':
        return 2;
      case '.|':
        return 1;
      default:
        return 0;
    }
  }).filter(n => n !== 0);
}
```