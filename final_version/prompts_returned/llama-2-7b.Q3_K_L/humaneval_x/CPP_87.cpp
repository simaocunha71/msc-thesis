/*
You are given a 2 dimensional data, as a nested vectors,
which is similar to matrix, however, unlike matrices,
each row may contain a different number of columns.
Given lst, and integer x, find integers x in the vector,
and return vector of vectors, {{x1, y1}, {x2, y2} ...} such that
each vector is a coordinate - {row, columns}, starting with 0.
Sort coordinates initially by rows in ascending order.
Also, sort coordinates of the row by columns in descending order.

Examples:
get_row({
  {1,2,3,4,5,6},
  {1,2,3,4,1,6},
  {1,2,3,4,5,1}
}, 1) == {{0, 0}, {1, 4}, {1, 0}, {2, 5}, {2, 0}}
get_row({}, 1) == {}
get_row({{}, {1}, {1, 2, 3}}, 3) == {{2, 2}}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<vector<int>> get_row(vector<vector<int>> lst, int x){
    vector<vector<int>> res;
    for (auto row:lst){
        sort(row.begin(), row.end());
        
        //find elements of a vector in the column of the row
        auto col_elems = find(row.begin(), row.end(), x);
        if (!col_elems.empty()){//we have an element here
            res.push_back({col_elems[0], row.size() - 1});//sort them in descending order
        }else{//no element found yet
            for (int i = 0;i < row.size();i++){
                if(x == row[i]) res.push_back({i, row.size()-1}); //sort them in descending order
            }
        }
    }
    return res;
}
int main(){
    vector<vector<int>> lst = {{0, 5}, {7,