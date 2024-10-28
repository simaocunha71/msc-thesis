    int n = arr.size();
    if(n == 0)
        return true;
    int count = 0;

B:
    for(int i = 0; i < n - 1; i++){
        if(arr[i] > arr[i + 1])
            count++;
    }

C:
    if(arr[n - 1] > arr[0])
        count++;

D:
    return count <= 1;
}

// Driver code
int main() {
    vector<int> arr1 = {3, 4, 5, 1, 2};
    vector<int> arr2 = {3, 5, 4, 1, 2};
    cout << move_one_ball(arr1) << endl;
    cout << move_one_ball(arr2) << endl;
    return 0;
}

*/

//Solution/C++/move_one_ball.cpp
#include <vector>
using namespace std;

bool move_one_ball(vector<int> arr) {
    int n = arr.size();
    if(n == 0)
        return true;
    int count = 0;
    for(int i = 0; i < n - 1; i++){
        if(arr[i] > arr[i + 1])
            count++;
    }
    if(arr[n - 1] > arr[0])
        count++;
    return count <= 1;
}

//Solution/C++/move_one_ball_test.cpp
#include "gtest/gtest.h"
#include "move_one_ball.cpp"

TEST(MoveOneBallTest, HandlesEmptyVector) {
    vector<int> arr = {};
    EXPECT_EQ(move_one_ball(arr), true);
}

TEST(MoveOneBallTest, HandlesSortedVector) {
    vector<int> arr = {1, 2, 3, 4, 5};
    EXPECT_EQ(move_one_ball(arr), true);
}

TEST(MoveOneBallTest,