```java
const sortNumbers = (numbers) => {
  var numberals = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
  var sorted = numbers.split(' ').sort(function(a, b) {
    return numberals.indexOf(a) - numberals.indexOf(b);
  }).join(' ');
  return sorted;
}
```