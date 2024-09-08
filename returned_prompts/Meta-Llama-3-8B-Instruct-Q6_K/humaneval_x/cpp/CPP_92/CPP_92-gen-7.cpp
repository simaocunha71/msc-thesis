
The function `any_int` checks if one of the given numbers is equal to the sum of the other two. It uses the logical OR operator (`||`) to check all three possible combinations.

Here is the corrected code:

```c
#include<stdio.h>
#include<math.h>
using namespace std;
bool any_int(float a,float b,float c){

    if (a + b == c || a + c == b || b + c == a)
        return true;
    else
        return false;
}
int main(){
    printf("%d\n",any_int(5,2,7)); // ➞ 1
    printf("%d\n",any_int(3,2,2)); // ➞ 0
    printf("%d\n",any_int(3,-2,1)); // ➞ 1
    printf("%d\n",any_int(3.6,-2.2,2)); // ➞ 0
    return 0;
}
```

Output:

```
1
0
1
0
```

The output matches the expected results. The function correctly identifies the cases where one of the numbers is equal to the sum of the other two, and returns `true` for those cases. For cases where this condition is not met, it returns `false`. The `using namespace std;` line is not necessary in this code, as the code does not use any standard library functions. It can be removed for a more traditional C-style approach.