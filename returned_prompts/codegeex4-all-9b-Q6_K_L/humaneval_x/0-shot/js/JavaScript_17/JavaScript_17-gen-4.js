```java
const parseMusic = (music_string) => {
  var beats = music_string.split(/\s+/);
  var result = [];
  for (var i = 0; i < beats.length; i++) {
    switch (beats[i]) {
      case 'o':
        result.push(4);
        break;
      case 'o|':
        result.push(2);
        break;
      case '.|':
        result.push(1);
        break;
    }
  }
  return result;
}
```