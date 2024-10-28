```java
const fileNameCheck = (file_name) => {
  let [name, ext] = file_name.split('.')
  if (ext != 'txt' && ext != 'exe' && ext != 'dll') { return 'No' }
  if (!(/[a-zA-Z]/.test(name[0]))) { return 'No' }
  if (name.length - name.replace(/[0-9]/g, '').length > 3) { return 'No' }
  return 'Yes'
}
```
