```java
const splitWords = (txt) => {
  if (txt.split(' ').length > 1) {
    return txt.split(' ');
  } else if (txt.split(',').length > 1) {
    return txt.split(',');
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt[i] >= 'a' && txt[i] <= 'z' && txt.charCodeAt(i) % 2 == 1) {
        count++;
      }
    }
    return count;
  }
}
```
