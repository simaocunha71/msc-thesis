```java
const numericalLetterGrade = (grades) => {
  var out = []
  for (i = 0; i < grades.length; i++) {
    if (grades[i] == 4.0) { out.push('A+'); }
    else if (grades[i] > 3.7) { out.push('A'); }
    else if (grades[i] > 3.3) { out.push('A-'); }
    else if (grades[i] > 3.0) { out.push('B+'); }
    else if (grades[i] > 2.7) { out.push('B'); }
    else if (grades[i] > 2.3) { out.push('B-'); }
    else if (grades[i] > 2.0) { out.push('C+'); }
    else if (grades[i] > 1.7) { out.push('C'); }
    else if (grades[i] > 1.3) { out.push('C-'); }
    else if (grades[i] > 1.0) { out.push('D+'); }
    else if (grades[i] > 0.7) { out.push('D'); }
    else if (grades[i] > 0.0) { out.push('D-'); }
    else { out.push('E'); }
  }
  return out
}
```
