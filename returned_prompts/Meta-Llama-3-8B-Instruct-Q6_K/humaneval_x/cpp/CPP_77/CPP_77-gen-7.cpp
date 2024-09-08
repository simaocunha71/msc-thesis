    int i = round(cbrt(a));
    if(i*i*i == a) return true;
    else return false;
}

int main(){
    printf("%d\n",iscuber(1)); // true
    printf("%d\n",iscuber(2)); // false
    printf("%d\n",iscuber(-1)); // true
    printf("%d\n",iscuber(64)); // true
    printf("%d\n",iscuber(0)); // true
    printf("%d\n",iscuber(180)); // false
    return 0;
} 

R:
The problem is asking to create a function that checks if the given integer is a perfect cube or not. A perfect cube is an integer that is the cube of an integer. For example, 1, 8, 27, 64, 125 are perfect cubes.

The function `iscuber(int a)` is defined to solve this problem. It uses the `cbrt` function from the `math.h` library to calculate the cube root of the given integer. The `round` function is used to round the result to the nearest integer.

The function then checks if the cube of the rounded result is equal to the given integer. If it is, the function returns `true`, indicating that the integer is a perfect cube. Otherwise, it returns `false`.

The `main` function is used to test the `iscuber` function with different inputs. The results are printed to the console. 

Here is the code:

```c
#include<stdio.h>
#include<math.h>
using namespace std;
bool iscuber(int a){
    int i = round(cbrt(a));
    if(i*i*i == a) return true;
    else return false;
}

int main(){
    printf("%d\n",iscuber(1)); // true
    printf("%d\n",iscuber(2)); // false
    printf("%d\n",iscuber(-1)); // true
    printf("%d\n",iscuber(64)); // true
    printf("%d\n",iscuber(0)); // true
    printf("%d\n",iscuber(180)); // false
    return 0;
}
```

When you run this code, it will print the following output:

```
1
0
1
1
1
0
```

This indicates that the function is working correctly. The function correctly identifies the perfect cubes and returns `true` for them, and returns