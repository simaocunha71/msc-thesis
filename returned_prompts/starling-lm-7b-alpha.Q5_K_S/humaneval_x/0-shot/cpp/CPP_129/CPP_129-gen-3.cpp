    int n = grid.size();
    vector<int> res(k);
    int i = 0, j = 0;
    int d = 0;
    for(int a = 0; a < k; a++) {
        if(d == 0) {
            if(i < n - 1) {
                i++;
            } else {
                i = 0;
                j++;
                if(j < n) {
                    d = 1;
                } else {
                    d = -1;
                    j = n - 1;
                }
            }
        } else if(d == 1) {
            if(j < n - 1) {
                j++;
            } else {
                j = 0;
                i++;
                d = 0;
            }
        } else {
            if(i > 0) {
                i--;
            } else {
                i = 0;
                j--;
                d = 1;
            }
        }
        res[a] = grid[i][j];
    }
    return res;
}

int main() {
    vector<vector<int>> grid = {{1,2,3}, {4,5,6}, {7,8,9}};
    int k = 3;
    printf("%d\n", minPath(grid, k)[0]);
}

*/







/*
Given a string S, we can transform by replacing all lowercase 'a' with uppercase 'A' get T.

Besides, every lowercase letter in T will be replaced by the corresponding uppercase letter.
For example, "AAbBcC" will be transformed to "AABBCC".

Return the length of the longest substring S, all of whose letters occur in T.

Example 1:
Input: S = "aBBbCc" , T = "AaaBBbcC"
Output: 4
Explanation: Here, the longest substring with all letters in T is "BBbb".

Example 2:
Input