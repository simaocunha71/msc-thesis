```java
const fileNameCheck = (file_name) => {
  var nums = file_name.replace(/[^\d]/g, '').length
  var parts = file_name.split('.')
  if (nums > 3 || parts.length != 2 || !/[a-zA-Z]/.test(parts[0][0]) || !['txt', 'exe', 'dll'].includes(parts[1])) {
    return 'No'
  } else {
    return 'Yes'
  }
}
```
