```java
const fileNameCheck = (file_name) => {
  let digit_count = 0
  let dot_count = 0
  let alpha_count = 0
  let ext = ''
  for (let i = 0; i < file_name.length; i++) {
    if (file_name[i].match(/[0-9]/)) {digit_count++}
    else if (file_name[i] === '.') {dot_count++}
    else if (file_name[i].match(/[A-Za-z]/)) {alpha_count++}
  }
  if (dot_count === 1 && digit_count < 4) {
    let arr = file_name.split('.')
    if (arr.length === 2 && arr[1] === 'txt' || arr[1] === 'exe' || arr[1] === 'dll') {
      if (alpha_count === file_name.length - 1) {
        return 'Yes'
      }
    }
  }
  return 'No'
}
```
