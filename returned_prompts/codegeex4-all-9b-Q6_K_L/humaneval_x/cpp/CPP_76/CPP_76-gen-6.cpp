```cpp
#include <math.h>

bool is_simple_power(int x, int n) {
    if (x == 1) return true;
    if (n == 1) return false;
    int p = 0;
    while (x > 1) {
        if (x % n != 0) return false;
        x /= n;
        p++;
    }
    return true;
}
```

B:
```cpp
#include <math.h>

bool is_simple_power(int x, int n) {
    if (x == 1) return true;
    if (n == 1) return false;
    int p = 0;
    while (x > 1) {
        if (x % n != 0) return false;
        x /= n;
    }
    return p > 0;
}
```

C:
```cpp
#include <math.h>

bool is_simple_power(int x, int n) {
    if (x == 1) return true;
    if (n == 1) return false;
    int p = 0;
    while (x > 1) {
        if (x % n != 0) return false;
        x /= n;
        p++;
    }
    return p > 0;
}
```

D:
```cpp
#include <math.h>

bool is_simple_power(int x, int n) {
    if (x == 1) return true;
    if (n == 1) return false;
    int p = 0;
    while (x > 1) {
        if (x % n != 0) return false;
    }
    return p > 0;
}
```

E:
```cpp
#include <math.h>

bool is_simple_power(int x, int n) {
    if (x == 1) return true;
    if (n == 1) return false;
    int p = 0;
    while (x > 1) {
        if (x % n != 0) return false;
        x /= n;
        p++;
    }
    return p > 0 || x == 1;
}
```

F:
```cpp
#include <math.h>

bool is_simple_power(int x, int n) {
    if (x == 1) return true;
    if (n == 1) return false;
    int p = 0;
    while (x > 1) {
        if (x