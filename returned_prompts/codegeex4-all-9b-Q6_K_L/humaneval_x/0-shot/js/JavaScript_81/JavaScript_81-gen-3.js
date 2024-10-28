```java
const numericalLetterGrade = (grades) => {
  let result = []
  for (let i = 0, len = grades.length; i < len; i++) {
    if (grades[i] == 4.0) {
      result.push('A+')
    } else if (grades[i] > 3.7) {
      result.push('A')
    } else if (grades[i] > 3.3) {
      result.push('A-')
    } else if (grades[i] > 3.0) {
      result.push('B+')
    } else if (grades[i] > 2.7) {
      result.push('B')
    } else if (grades[i] > 2.3) {
      result.push('B-')
    } else if (grades[i] > 2.0) {
      result.push('C+')
    } else if (grades[i] > 1.7) {
      result.push('C')
    } else if (grades[i] > 1.3) {
      result.push('C-')
    } else if (grades[i] > 1.0) {
      result.push('D+')
    } else if (grades[i] > 0.7) {
      result.push('D')
    } else if (grades[i] > 0.0) {
      result.push('D-')
    } else if (grades[i] == 0.0) {
      result.push('E')
    }
  }
  return result
}
```
