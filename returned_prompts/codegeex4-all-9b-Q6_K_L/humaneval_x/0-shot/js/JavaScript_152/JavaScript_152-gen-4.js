```java
const compare = (game, guess) => {
  return game.map((item, index) => Math.abs(item - guess[index]))
}
```
