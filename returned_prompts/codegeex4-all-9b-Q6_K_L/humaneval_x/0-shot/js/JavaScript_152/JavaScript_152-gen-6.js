```java
const compare = (game, guess) => {
  let out = []
  for (let i = 0; i < game.length; i++) {
    out.push(Math.abs(game[i] - guess[i]))
  }
  return out
}
```
