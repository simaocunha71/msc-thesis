```java
const fileNameCheck = (file_name) => {
  let [name, extension] = file_name.split(/\.(?=[^.]+$)/)
  if (name.length > 3 || extension == '') return 'No'
  let hasDigit = name.match(/\d/g)
  if (hasDigit != null && hasDigit.length > 3) return 'No'
  let startsWithLetter = name[0].match(/[a-z]/gi)
  if (startsWithLetter == null) return 'No'
  let validExtensions = ['txt', 'exe', 'dll']
  if (validExtensions.includes(extension)) return 'Yes'
  return 'No'
}
```
