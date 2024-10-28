The solution is to define a function `compareOne` that takes two arguments `a` and `b`. The function checks the type of `a` and `b` and compares them accordingly. If both `a` and `b` are numbers, it compares them numerically. If one is a string and the other is a number, it converts the string to a number and compares them numerically. If both are strings, it compares them lexicographically. If the values are equal, it returns `null`.

Here is the implementation in JavaScript:
```
const compareOne = (a, b) => {
  if (typeof a === 'number' && typeof b === 'number') {
    return (a > b) ? a : ((a < b) ? b : null);
  } else if (typeof a === 'number' && typeof b === 'string') {
    return (parseFloat(b) > a) ? b : ((parseFloat(b) < a) ? a : null);
  } else if (typeof a === 'string' && typeof b === 'number') {
    return (a > String(b)) ? a : ((a < String(b)) ? String(b) : null);
  } else if (typeof a === 'string' && typeof b === 'string') {
    return (a > b) ? a : ((a < b) ? b : null);
  }
};
```
This function works as expected:
```
console.log(compareOne(1, 2.5)); // 2.5
console.log(compareOne(1, "2,3")); // "2,3"
console.log(compareOne("5,1", "6")); // "6"
console.log(compareOne("1", 1)); // null
```  🤖
```python
def compare_one(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a if a > b else b if a < b else None
    elif isinstance(a, int) and isinstance(b, str):
        return b if float(b.replace(',', '')) > a else a if float(b.replace(',', '')) < a else None
    elif isinstance(a, str) and isinstance(b, int):
        return a if a > str(b) else str(b) if a < str(b) else None
    elif isinstance(a, str) and isinstance(b, str):
        return a if a > b else b if a < b else