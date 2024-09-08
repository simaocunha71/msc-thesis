    int count = 0;
    for(int i = 1; i < 10; i++){
        for(int j = 0; j < n; j++){
            if((i == 1 && j == 0) || (i == 1 && j == n-1)){
                count++;
            }
        }
    }
    return count;
}

int main(){
    int n;
    printf("Enter a positive integer n: ");
    scanf("%d", &n);
    int res = starts_one_ends(n);
    printf("Count of n-digit positive integers that start or end with 1: %d", res);
    return 0;
}
B:
#include <bits/stdc++.h>
using namespace std;

int countNumbers(int n) {
    int count = 0;
    for (int i = 1; i <= 9; i++) {
        if (i == 1 || i % 10 == 1) {
            count++;
        }
        for (int j = 0; j < n - 1; j++) {
            count += 10;
        }
    }
    return count;
}

int main() {
    int n;
    cin >> n;
    cout << countNumbers(n) << endl;
    return 0;
}
C:
#include <bits/stdc++.h>
using namespace std;

int countNumbers(int n) {
    int count = 0;
    for (int i = 1; i <= 9; i++) {
        if (i == 1 || i % 10 == 1) {
            count++;
        }
        for (int j = 0; j < n - 1; j++) {
            count += 10;
        }
    }
    return count;
}

int main() {
    int n;
    cin >> n;
    cout << countNumbers(n) << endl;
    return 0;
}
D:
#include <bits/stdc++.h>
using namespace std;

int countNumbers(int n) {
    int count = 0;
    for (int i = 1; i <= 9; i++) {
        if (i == 1 || i % 10 == 1) {
            count++;
        }
        for (int j = 0; j < n - 1; j++) {
            count += 10;
        }
    }
    return count;
}

int main() {
    int n;
    cin >> n;
    cout <<