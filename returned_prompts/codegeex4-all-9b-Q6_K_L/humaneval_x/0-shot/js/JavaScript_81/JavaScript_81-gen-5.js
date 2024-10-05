```java
const numericalLetterGrade = (grades) => {
  return grades.map(g => {
    if (g > 3.7) { return 'A' }
    if (g > 3.3) { return 'A-' }
    if (g > 3) { return 'B+' }
    if (g > 2.7) { return 'B' }
    if (g > 2.3) { return 'B-' }
    if (g > 2) { return 'C+' }
    if (g > 1.7) { return 'C' }
    if (g > 1.3) { return 'C-' }
    if (g > 1) { return 'D+' }
    if (g > 0.7) { return 'D' }
    if (g > 0) { return 'D-' }
    if (g == 0) { return 'E' }
  })
}
```
