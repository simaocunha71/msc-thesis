    int remainder;
    string result="";
    while(N>0){
        remainder = N % 2;
        N = N / 2;
        result = to_string(remainder) + result;
    }
    return result;
}

int main(){
    int N;
    scanf("%d", &N);
    printf("%s\n", solve(N).c_str());
    return 0;
}
*/

#include <iostream>
#include <string>
using namespace std;

string solve(int N) {
    int remainder;
    string result = "";
    while (N > 0) {
        remainder = N % 2;
        N = N / 2;
        result = to_string(remainder) + result;
    }
    return result;
}

int main() {
    int N;
    cin >> N;
    cout << solve(N) << endl;
    return 0;
}

/*
test:
    assert solve(1000) == "1"
    assert solve(150) == "110"
    assert solve(147) == "1100"
*/
```

### Python
```python
# Python

def solve(N):
    return bin(N)[2:]

N = int(input().strip())
print(solve(N))

# test
assert solve(1000) == "1"
assert solve(150) == "110"
assert solve(147) == "1100"
```

### JavaScript
```javascript
// JavaScript

function solve(N){
    return N.toString(2);
}

let N = parseInt(readLine(), 10);
console.log(solve(N));

// test
console.assert(solve(1000) === "1")
console.assert(solve(150) === "110")
console.assert(solve(147) === "1100")
```

### Java
```java
// Java

import java.