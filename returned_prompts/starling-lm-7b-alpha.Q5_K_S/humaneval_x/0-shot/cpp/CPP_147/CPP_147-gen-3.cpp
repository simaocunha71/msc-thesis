    int res = 0;
    vector<int> a;
    for(int i = 1; i <= n; i++)
        a.push_back(i * i - i + 1);

    for(int i = 0; i < n; i++)
        for(int j = i + 1; j < n; j++)
            for(int k = j + 1; k < n; k++)
                if((a[i] + a[j] + a[k]) % 3 == 0)
                    res++;
    return res;
}
int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", get_matrix_triples(n));
}





ANSWER:
No
EXPLANATION:
The problem can be solved with a simple for loop, with the time complexity being O(n^3) and space complexity being O(1).

CORRECT SOLUTION:
```
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    int cnt = 0;
    for(int i = 1; i <= n; i++) {
        for(int j = i + 1; j <= n; j++) {
            for(int k = j + 1; k <= n; k++) {
                if((i * i - i + 1 + j * j - j + 1 + k * k - k + 1) % 3 == 0) {
                    cnt++;
                }
            }
        }
    }
    cout << cnt;
}
```











































































































