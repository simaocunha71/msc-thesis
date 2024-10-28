```java
const fileNameCheck = (file_name) => {
  let t = file_name.split(/\./)
  if (t.length != 2) {return 'No'}
  if (t[0].length == 0 || t[1] != "txt" && t[1] != "exe" && t[1] != "dll") {return 'No'}
  if (t[0].match(/\d/g) && t[0].match(/\d/g).length > 3) {return 'No'}
  if (t[0].match(/^[0-9]/g)) {return 'No'}
  return 'Yes'
}
```
