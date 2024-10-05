    if (n < 0) {
        return -1;
    }
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    int dp[n + 1][2];
    dp[1][0] = dp[1][1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1];
        dp[i][1] = dp[i - 1][0];
    }
    return 2 * dp[n][0] + dp[n][1];
}
int main() {
    int n;
    scanf("%d", &n);
    printf("%d", starts_one_ends(n));
    return 0;
}

*/

//Task1/main.cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int countNums(int n) {
    if (n == 0) {
        return 0;
    }

    vector<int> dp(n + 1, 0);
    dp[0] = dp[1] = 1;

    for (int i = 2; i <= n; i++) {
        dp[i] = 2 * dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}

int main() {
    int n;
    cin >> n;

    cout << countNums(n) << endl;

    return 0;
}

//Task2/main.cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int countNums(int n) {
    if (n == 0) {
        return 0;
    }

    vector<int> dp(n + 1, 0);
    dp[0] = dp