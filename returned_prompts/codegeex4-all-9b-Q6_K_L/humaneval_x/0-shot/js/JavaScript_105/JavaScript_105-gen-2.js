```java
const byLength = (arr) => {
  let sorted = arr.filter(num => num > 0 && num < 10).sort((a, b) => a - b);
  let reversed = sorted.reverse();
  let mapped = reversed.map(num => {
    switch (num) {
      case 1:
        return 'One';
      case 2:
        return 'Two';
      case 3:
        return 'Three';
      case 4:
        return 'Four';
      case 5:
        return 'Five';
      case 6:
        return 'Six';
      case 7:
        return 'Seven';
      case 8:
        return 'Eight';
      case 9:
        return 'Nine';
      default:
        return '';
    }
  });
  return mapped;
}
```
