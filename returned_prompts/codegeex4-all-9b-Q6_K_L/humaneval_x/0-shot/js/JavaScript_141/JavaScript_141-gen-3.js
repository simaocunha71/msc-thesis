```java
const fileNameCheck = (file_name) => {
  let digit_count = 0
  let dot_count = 0
  let after_dot = ''
  let before_dot = ''
  for (let i = 0; i < file_name.length; i++) {
    if (file_name[i] >= '0' && file_name[i] <= '9') digit_count++
    if (file_name[i] === '.') {
      dot_count++
      if (i < file_name.length - 1) {
        after_dot = file_name.substring(i + 1)
      }
    } else if (i === 0 && (file_name[i] < 'a' || file_name[i] > 'z') && (file_name[i] < 'A' || file_name[i] > 'Z')) return 'No'
    else before_dot += file_name[i]
  }
  if (dot_count > 1 || digit_count > 3 || after_dot === '' || ['txt', 'exe', 'dll'].indexOf(after_dot) === -1) return 'No'
  return 'Yes'
}
```