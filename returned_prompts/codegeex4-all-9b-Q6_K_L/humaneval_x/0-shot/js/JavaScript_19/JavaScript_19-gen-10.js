```java
const sortNumbers = (numbers) => {
  return numbers.split(' ')
                .sort((a, b) => ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
                                .indexOf(a) - ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
                                .indexOf(b))
                .join(' ');
}
```
