
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cassert>
using namespace std;

// Find the minimum path from (0, 0) to (m-1, n-1) in a grid of size m*n
// with the given weights.
// Returns the minimum path weight.
int minPath(const vector<vector<int>>& weights, int m, int n) {
  // Create a 2D array dp where dp[i][j] represents the minimum weight
  // from (0, 0) to (i, j)
  vector<vector<int>> dp(m + 1, vector<int>(n + 1, 10000000));

  // Initialize the first row and column
  for (int i = 1; i <= m; i++) {
    dp[i][0] = i;
  }
  for (int j = 1; j <= n; j++) {
    dp[0][j] = j;
  }

  // Fill in the table
  for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
      dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + weights[i - 1][j - 1];
    }
 