    long long result = 1;
    for(int i = n; i > 0; i--){
        long long fact = 1;
        for(int j = i; j > 0; j--){
            fact *= j;
        }
        result *= fact;
    }
    return result;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%lld\n", special_factorial(n));
    return 0;
}

*/

#include<iostream>
using namespace std;

long long special_factorial(int n){
    long long result = 1;
    for(int i = n; i > 0; i--){
        long long fact = 1;
        for(int j = i; j > 0; j--){
            fact *= j;
        }
        result *= fact;
    }
    return result;
}

int main(){
    int n;
    cin >> n;
    cout << special_factorial(n) << endl;
    return 0;
}
```

### Python

```python
import math
def special_factorial(n):
    if n == 0:
        return 1
    else:
        return math.factorial(n) * special_factorial(n-1)

n = int(input())
print(special_factorial(n))
```

### C++

```c++
#include<iostream>
#include<cmath>
using namespace std;

long long special_factorial(int n){
    if(n == 0){
        return 1;
    }
    else{
        return tgamma(n+1);
    }
}

int main(){
    int n;
    cin >> n;
    cout << special_factorial(n) << endl;
    return 0;
}
```

### Java

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n