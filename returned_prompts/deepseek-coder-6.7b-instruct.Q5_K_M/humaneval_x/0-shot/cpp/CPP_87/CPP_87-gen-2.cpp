Here's the code with comments explaining each part:

```cpp
#include<iostream>
#include<vector>
using namespace std;

// function to find integer x in the vector and return its coordinates
vector<vector<int>> get_row(vector<vector<int>> lst, int x){

    vector<vector<int>> result;  // to store the coordinates of x

    // loop through each row of the 2D vector
    for(int i=0; i<lst.size(); i++){

        // loop through each element in the current row
        for(int j=0; j<lst[i].size(); j++){

            // if the current element is x, store its coordinates
            if(lst[i][j] == x){
                result.push_back({i, j});
            }
        }
    }

    // return the coordinates of x
    return result;
}

int main() {

    // test the function
    vector<vector<int>> lst = {{1,2,3,4,5,6}, {1,2,3,4,1,6}, {1,2,3,4