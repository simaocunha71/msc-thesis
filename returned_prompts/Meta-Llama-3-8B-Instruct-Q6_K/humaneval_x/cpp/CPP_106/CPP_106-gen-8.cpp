    vector<int> result(n);
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0) // if i is even
            result[i-1] = i; // factorial
        else
            result[i-1] = i; // sum of numbers from 1 to i
    }
    return result;
}

int main()
{
    int n = 5;
    vector<int> result = f(n);
    for(int i = 0; i < n; i++)
        printf("%d ", result[i]);
    return 0;
}
C:
#include <iostream>
#include <vector>

using namespace std;

vector<int> f(int n) {
    vector<int> result(n);
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            result[i-1] = i;
        } else {
            int sum = 0;
            for (int j = 1; j <= i; j++) {
                sum += j;
            }
            result[i-1] = sum;
        }
    }
    return result;
}

int main() {
    int n = 5;
    vector<int> result = f(n);
    for (int i = 0; i < n; i++) {
        cout << result[i] << " ";
    }
    return 0;
}
B:
#include <iostream>
#include <vector>

using namespace std;

vector<int> f(int n) {
    vector<int> result(n);
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            result[i-1] = 1; // factorial
        } else {
            int sum = 0;
            for (int j = 1; j <= i; j++) {
                sum += j;
            }
            result[i-1] = sum;
        }
    }
    return result;
}

int main() {
    int n = 5;
    vector<int> result = f(n);
    for (int i = 0; i < n; i++) {
        cout << result[i] << " ";
    }
    return 0;
}
D:
#include <iostream>
#include <vector>

using namespace std;

vector<int> f(int n) {
    vector<int> result(n);
    for (int i = 1; i <=