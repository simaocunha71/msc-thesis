    vector<vector<int>> result;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                result.push_back({i, j});
            }
        }
    }
    return result;
}

int main(){

    return 0;
}

Solution:
The solution is quite straightforward, we are traversing through the 2-dimensional vector, checking each element if it's equal to the given integer x. If yes, we are adding the coordinate pair {i, j} to our result vector. The coordinates are being stored as {row, column} starting from 0.

In the case of sorting, it's not required since the problem statement does not specify the sorting order. However, if you would like to sort the result by rows in ascending order and by columns in descending order, you can use the std::sort function from the algorithm library. Please note that you need to provide a custom comparator for sorting by rows in ascending and by columns in descending order.
*/

// Add the following lines to the solution to sort the coordinates:

// bool compare(vector<int> &a, vector<int> &b){
//     if(a[0] == b[0]) return a[1] > b[1];
//     return a[0] < b[0];
// }

// And then you can call the sort function with your result vector as follows:

// sort(result.begin(), result.end(), compare);

// This will sort your result vector in ascending order of rows and in descending order of columns.

/*
Please note that this solution assumes that the input vector is not empty and does not contain empty sub-vectors. If these conditions might not always hold true, you should add error checking for these cases.
*/

// Add the following lines to the solution to handle these cases:

// if(lst.empty() || any_of(lst.begin(), lst.end(), [](const vector<int>& v) { return v.empty(); }))
//     return result