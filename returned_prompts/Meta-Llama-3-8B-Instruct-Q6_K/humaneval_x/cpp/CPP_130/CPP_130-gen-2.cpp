    vector<int> result;
    result.push_back(3);
    if(n == 0) return result;

    if(n % 2 == 0) {
        result.push_back(1 + n / 2);
        for(int i = 3; i <= n; i += 2) {
            result.push_back(result[i-1] + result[i-2]);
        }
    }
    else {
        result.push_back(1 + (n-1) / 2);
        for(int i = 4; i <= n; i += 2) {
            result.push_back(result[i-1] + result[i-2]);
        }
    }
    return result;
}
int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    vector<int> result = tri(n);
    printf("The first %d numbers of the Tribonacci sequence: ", n+1);
    for(int i = 0; i <= n; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

B:
#include <iostream>
#include <vector>

using namespace std;

vector<int> tribonacci(int n) {
    vector<int> result;
    result.push_back(3);

    for(int i = 1; i <= n; i++) {
        if(i % 2 == 0) {
            result.push_back(1 + i / 2);
        } else {
            if(i == 1) {
                result.push_back(1);
            } else {
                result.push_back(result[i-1] + result[i-2] + result[i-3]);
            }
        }
    }

    return result;
}

int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    vector<int> result = tribonacci(n);
    cout << "The first " << n + 1 << " numbers of the Tribonacci sequence: ";
    for(int i = 0; i <= n; i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}C:
#include <iostream>
#include <vector>

using namespace std;

vector<int> tribonacci(int n) {
    vector<int> result;
    result.push_back(3);

    if(n == 0) {
        return result;
    }

    if(n % 2