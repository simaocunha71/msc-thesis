```java
const fileNameCheck = (file_name) => {
  let dotCount = 0;
  let digitCount = 0;
  let alphaCount = 0;
  let ext = '';
  for (let i = 0; i < file_name.length; i++) {
    let c = file_name[i];
    if (c == '.') {
      dotCount++;
      ext = file_name.substring(i + 1);
    } else if (c >= '0' && c <= '9') {
      digitCount++;
    } else if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
      alphaCount++;
    }
  }
  if (digitCount > 3 || dotCount != 1 || ext.length != 3 || !['txt', 'exe', 'dll'].includes(ext) || alphaCount == 0) {
    return 'No';
  }
  return 'Yes';
}
```
