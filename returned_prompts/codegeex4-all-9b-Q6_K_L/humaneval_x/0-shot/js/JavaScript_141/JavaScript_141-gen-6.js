```java
const fileNameCheck = (file_name) => {
  let split_file_name = file_name.split('.')
  if (split_file_name.length != 2) { return 'No' }
  let file_extension = split_file_name[1]
  if (file_extension != 'txt' && file_extension != 'exe' && file_extension != 'dll') { return 'No' }
  let file_name_without_extension = split_file_name[0]
  let digit_counter = 0
  for (let i = 0; i < file_name_without_extension.length; i++) {
    if (!isNaN(parseInt(file_name_without_extension[i]))) { digit_counter++ }
  }
  if (digit_counter > 3) { return 'No' }
  if (file_name_without_extension.length == 0) { return 'No' }
  let first_char = file_name_without_extension.charAt(0).toLowerCase()
  if (!isLetter(first_char)) { return 'No' }
  return 'Yes'
}

function isLetter(char) {
  return char >= 'a' && char <= 'z'
}
```
