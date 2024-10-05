```java
const splitWords = (txt) => {
  if (txt.indexOf(' ') !== -1) {
    return txt.split(' ');
  } else if (txt.indexOf(',') !== -1) {
    return txt.split(',');
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt[i] === txt[i].toLowerCase() && txt[i].charCodeAt() % 2 !== 0) {
        count++;
      }
    }
    return count;
  }
}
```
