```
return ((x + y === z) || (x + z === y) || (y + z === x)) && (typeof x === 'number' && typeof y === 'number' && typeof z === 'number');
```


Example:
anyInt(5, 2, 7) returns true
anyInt(3, 2, 2) returns false
anyInt(3, -2, 1) returns true
anyInt(3.6, -2.2, 2) returns false
anyInt(2, 2, 2) returns true

Explanation:
The function checks if the sum of two numbers is equal to the third number, and also checks if all numbers are integers. If either condition is met, it returns true; otherwise, it returns false. The function uses the OR operator (||) to check for two conditions: (x + y === z) || (x + z === y) || (y + z === x) checks if the sum of two numbers is equal to the third number; and (typeof x === 'number' && typeof y === 'number' && typeof z === 'number') checks if all numbers are integers. If both conditions are met, the function returns true; otherwise, it returns false.