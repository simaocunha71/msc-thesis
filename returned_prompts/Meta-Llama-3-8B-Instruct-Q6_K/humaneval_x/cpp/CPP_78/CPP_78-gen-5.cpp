    int count=0;
    for(int i=0;i<num.length();i++){
        if(num[i]=='2' || num[i]=='3' || num[i]=='5' || num[i]=='7' || num[i]=='B' || num[i]=='D'){
            count++;
        }
    }
    return count;
}
int main(){
    string num="ABED1A33";
    int res = hex_key(num);
    printf("Number of hexadecimal digits that are primes: %d\n",res);
    return 0;
}

Solution:
The solution is straightforward. We just need to iterate through the input string and check if each character is either 2, 3, 5, 7, B or D. If it is, we increment a counter. Finally, we return the counter.

Here is the updated code with comments:

```c++
#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;

int hex_key(string num) {
    int count = 0;  // Initialize the counter to zero
    for(int i=0;i<num.length();i++){
        // Check if the current character is either 2, 3, 5, 7, B or D
        if(num[i]=='2' || num[i]=='3' || num[i]=='5' || num[i]=='7' || num[i]=='B' || num[i]=='D'){
            count++;  // If it is, increment the counter
        }
    }
    return count;  // Return the counter
}

int main(){
    string num="ABED1A33";
    int res = hex_key(num);
    printf("Number of hexadecimal digits that are primes: %d\n",res);
    return 0;
}
```

The output of this program will be:

```
Number of hexadecimal digits that are primes: 4
```

This is because the input string "ABED1A33" contains 4 hexadecimal digits that are primes: 2, B, D and 3.