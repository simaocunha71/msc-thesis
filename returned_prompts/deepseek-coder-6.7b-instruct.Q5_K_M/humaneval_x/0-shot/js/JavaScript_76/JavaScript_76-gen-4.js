  if (x === n || x === 1) {
    return true;
  } else if (x < 1 || n < 2) {
    return false;
  } else {
    for (let i = 2; i <= x; i++) {
      if (Math.pow(n, i) === x) {
        return true;
      }
    }
    return false;
  }
};
console.log(isSimplePower(1, 4));
console.log(isSimplePower(2, 2));
console.log(isSimplePower(8, 2));
console.log(isSimplePower(3, 2));
console.log(isSimplePower(3, 1));
console.log(isSimplePower(5, 3));

/*
This function works by checking if the result of raising the base number to the
integer power equals the original number. It starts by checking if the number is
equal to the base number or 1, in which case it returns true because those are
by definition simple powers of the base. If the number is less than 1 or the base
is less than 2, it returns false because those numbers cannot be simple powers.
Otherwise, it begins a loop that raises the base to integer powers until it finds
a match or exceeds the original number, in which case it returns false.
*/

/*
The time complexity of this function is O(x) because in the worst case scenario
it will have to iterate up to x times. The space complexity is O(1) because it
only uses a constant amount of space to store the variables i, x, and n.
*/
```

## C++

```C++
#include <iostream>
#include <cmath>

bool isSimplePower(int x, int n) {
    if (x == n || x == 1)
        return true;
    if (x < 1 || n < 2)
        return false;
    for (int i = 2; i <= x; i++) {
        if (std::pow(n, i) == x)
            return true;
    }
    return false;
}

int main() {
    std::cout << isSimplePower(1