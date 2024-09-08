    int p=2;
    while(p*p<=x){
        if(x%p==0){
            while(x%p==0)
                x=x/p;
            if(x==1)
                return true;
        }
        p=p+1;
    }
    if(x==n)
        return true;
    return false;
}
int main()
{
    printf("%d\n",is_simple_power(8,2));
    return 0;
}
B:
#include <iostream>
#include <cmath>
using namespace std;

bool is_simple_power(int x, int n) {
    if (n <= 0) {
        return false;
    }
    int i = 1;
    while (true) {
        int power = pow(n, i);
        if (power == x) {
            return true;
        }
        if (power > x) {
            return false;
        }
        i++;
    }
}

int main() {
    cout << is_simple_power(8, 2);
    return 0;
}
C:
#include <iostream>
#include <cmath>
using namespace std;

bool is_simple_power(int x, int n) {
    if (n <= 0) {
        return false;
    }
    int i = 1;
    double power = 1.0;
    while (true) {
        power = pow(n, i);
        if (power == x) {
            return true;
        }
        if (power > x) {
            return false;
        }
        i++;
    }
}

int main() {
    cout << is_simple_power(8, 2);
    return 0;
}
D:
#include <iostream>
#include <cmath>
using namespace std;

bool is_simple_power(int x, int n) {
    if (n <= 0) {
        return false;
    }
    int i = 1;
    while (true) {
        int power = (int) pow(n, i);
        if (power == x) {
            return true;
        }
        if (power > x) {
            return false;
        }
        i++;
    }
}

int main() {
    cout << is_simple_power(8, 2);
    return 0;
}
E:
#include <iostream>
#include <cmath>
using namespace std;

bool is_simple_power(int x, int n) {
    if (n <= 0) {
        return false;
    }
    int i = 1;
    while (true) {
        int power