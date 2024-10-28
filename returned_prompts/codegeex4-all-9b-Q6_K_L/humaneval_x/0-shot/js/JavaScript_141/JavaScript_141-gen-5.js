```java
const fileNameCheck = (file_name) => {
  let p1 = file_name.split('.')[0]
  let p2 = file_name.split('.')[1]
  if (p1.match(/[0-9]/g) == null || p1.match(/[0-9]/g).length <= 3 && p1.match(/^[a-zA-Z]/) != null && p2 == 'txt' || p2 == 'exe' || p2 == 'dll') {
    return 'Yes'
  }
  return 'No'
}
```