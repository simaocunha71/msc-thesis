```java
const fileNameCheck = (file_name) => {
  let nums = 0
  let dots = 0
  let txt = 0
  let exe = 0
  let dll = 0
  for (let i = 0; i < file_name.length; i++) {
    if (file_name[i] >= '0' && file_name[i] <= '9') {
      nums++
    }
    if (file_name[i] == '.') {
      dots++
    }
    if (file_name[i] == 't') {
      if (file_name[i + 1] == 'x' && file_name[i + 2] == 't') {
        txt++
      }
    }
    if (file_name[i] == 'e') {
      if (file_name[i + 1] == 'x' && file_name[i + 2] == 'e') {
        exe++
      }
    }
    if (file_name[i] == 'd') {
      if (file_name[i + 1] == 'l' && file_name[i + 2] == 'l') {
        dll++
      }
    }
  }
  if (nums <= 3 && dots == 1 && (txt == 1 || exe == 1 || dll == 1)) {
    return 'Yes'
  }
  return 'No'
}
```
