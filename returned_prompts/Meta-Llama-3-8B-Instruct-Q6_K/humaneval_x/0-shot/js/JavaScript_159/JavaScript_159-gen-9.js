```
const eat = (number, need, remaining) => {
  const total = number + Math.min(need, remaining);
  const left = remaining - (total - number);
  return [total, left];
}
```


Explanation:
The function takes three parameters: `number` (the number of carrots eaten so far), `need` (the number of carrots needed to eat), and `remaining` (the number of remaining carrots).

First, we calculate the total number of carrots eaten by adding the `number` and the minimum of `need` and `remaining`. This ensures that we eat no more carrots than there are remaining.

Then, we calculate the number of carrots left by subtracting the difference between the total and the initial number of eaten carrots from the initial remaining carrots.

Finally, we return an array containing the total number of eaten carrots and the number of carrots left.

Example inputs and outputs:
* eat(5, 6, 10) -> [11, 4]
* eat(4, 8, 9) -> [12, 1]
* eat(1, 10, 10) -> [11, 0]
* eat(2, 11, 5) -> [7, 0]