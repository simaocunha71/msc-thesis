    vector<int> a(n);
    int count = 0;
    for(int i = 1; i <= n; i++){
        a[i-1] = i * i - i + 1;
    }
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            for(int k = j + 1; k < n; k++){
                if((a[i] + a[j] + a[k]) % 3 == 0){
                    count++;
                }
            }
        }
    }
    return count;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", get_matrix_triples(n));
    return 0;
}

Answer:
The given problem can be solved by generating the sequence of a[i] = i * i - i + 1 for i = 1 to n and then checking all possible triplets of a[i], a[j], a[k] where i < j < k to see if their sum is a multiple of 3. Here is the C++ code to solve the problem:

```cpp
#include<stdio.h>
#include<vector>
using namespace std;

int get_matrix_triples(int n){
    vector<int> a(n);
    int count = 0;
    for(int i = 1; i <= n; i++){
        a[i-1] = i * i - i + 1;
    }
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            for(int k = j + 1; k < n; k++){
                if((a[i] + a[j] + a[k]) % 3 == 0){
                    count++;
                }
            }
        }
    }
    return count;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", get_matrix_triples(n));
    return 0;
}
```

This code first generates the sequence a[i] = i * i - i + 1 for i = 1 to n. Then it uses three nested loops to check all possible triplets of a[i], a[j], a[k] where i < j < k. If the sum of a[i], a[j], a[k] is a multiple of 3, it increments the count variable. Finally, it returns the