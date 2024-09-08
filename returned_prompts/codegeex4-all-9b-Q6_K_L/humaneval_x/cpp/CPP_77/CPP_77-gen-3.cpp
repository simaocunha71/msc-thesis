#include <iostream>
#include <cmath>
using namespace std;
bool isCube(int a) {
    if (a < 0) {
        a = -a;
    }
    int root = (int)round(cbrt(a));
    return (a == root * root * root);
}

B:
#include <iostream>
using namespace std;
bool isCube(int a) {
    if (a == 0) {
        return true;
    }
    for (int i = 0; i * i * i <= abs(a); i++) {
        if (i * i * i == abs(a)) {
            return true;
        }
    }
    return false;
}

C:
#include <iostream>
using namespace std;
bool isCube(int a) {
    if (a == 0) {
        return true;
    }
    for (int i = 0; i * i * i <= abs(a); i++) {
        if (i * i * i == abs(a)) {
            return true;
        }
    }
    return false;
}

D:
#include <iostream>
#include <cmath>
using namespace std;
bool isCube(int a) {
    if (a == 0) {
        return true;
    }
    int root = (int)round(cbrt(a));
    return (a == root * root * root);
}

E:
#include <iostream>
using namespace std;
bool isCube(int a) {
    if (a == 0) {
        return true;
    }
    for (int i = 0; i * i * i <= abs(a); i++) {
        if (i * i * i == abs(a)) {
            return true;
        }
    }
    return false;
}

F:
#include <iostream>
#include <cmath>
using namespace std;
bool isCube(int a) {
    if (a == 0) {
        return true;
    }
    int root = (int)round(cbrt(a));
    return (a == root * root * root);
}

G:
#include <iostream>
using namespace std;
bool isCube(int a) {
    if (a == 0) {
        return true;
    }
    for (int i = 0; i * i * i <= abs(a); i++) {
        if (i * i * i == abs(a)) {
            return true;
        }
    }
    return false;
}

H:
#include <iostream>
#include <cmath>
using namespace std