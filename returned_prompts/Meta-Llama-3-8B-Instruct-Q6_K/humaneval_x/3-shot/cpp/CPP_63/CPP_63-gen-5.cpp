    if (n <= 1) {
        return 0;
    }
    if (n == 2) {
        return 1;
    }
    int a = 0, b = 0, c = 1;
    for (int i = 3; i <= n; i++) {
        int d = a + b + c;
        a = b;
        b = c;
        c = d;
    }
    return c;
}
//or
#include<vector>
using namespace std;
int fibfib(int n){
    if(n <= 1) return 0;
    vector<int> fibfib_seq(3,0);
    fibfib_seq[1] = 0;
    fibfib_seq[2] = 1;
    for(int i = 3; i <= n; i++){
        fibfib_seq[i % 3] = fibfib_seq[(i-1)%3] + fibfib_seq[(i-2)%3] + fibfib_seq[(i-3)%3];
    }
    return fibfib_seq[n % 3];
}
//or
#include<vector>
using namespace std;
int fibfib(int n){
    if(n <= 1) return 0;
    vector<int> fibfib_seq(n + 1, 0);
    fibfib_seq[1] = 0;
    fibfib_seq[2] = 1;
    for(int i = 3; i <= n; i++){
        fibfib_seq[i] = fibfib_seq[i-1] + fibfib_seq[i-2] + fibfib_seq[i-3];
    }
    return fibfib_seq[n];
}