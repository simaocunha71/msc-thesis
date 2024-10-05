```java
const numericalLetterGrade = (grades) => {
  let s = []
  for (let i = 0; i < grades.length; i++) {
    if (grades[i] >= 4.0) { s.push('A+') }
    else if (grades[i] > 3.7) { s.push('A') }
    else if (grades[i] > 3.3) { s.push('A-') }
    else if (grades[i] > 3.0) { s.push('B+') }
    else if (grades[i] > 2.7) { s.push('B') }
    else if (grades[i] > 2.3) { s.push('B-') }
    else if (grades[i] > 2.0) { s.push('C+') }
    else if (grades[i] > 1.7) { s.push('C') }
    else if (grades[i] > 1.3) { s.push('C-') }
    else if (grades[i] > 1.0) { s.push('D+') }
    else if (grades[i] > 0.7) { s.push('D') }
    else if (grades[i] > 0.0) { s.push('D-') }
    else { s.push('E') }
  }
  return s
}
```
