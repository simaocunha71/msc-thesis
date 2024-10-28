```java
const splitWords = (txt) => {
  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      let charCode = txt.charCodeAt(i);
      if (charCode >= 97 && charCode <= 122 && (charCode % 2) != 0) {
        count++;
      }
    }
    return count;
  }
}
```
