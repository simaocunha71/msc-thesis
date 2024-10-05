
This is a pretty broad question, so I'll just provide some general feedback on each of your functions. 

You have some indentation issues in your has_close_elements function. This will cause compilation errors in C++. If you're going to use tabs for indentation, be sure that your editor is set to convert tabs to spaces (or vice versa). This is a common source of bugs in C++ code.

In your separate_paren_groups function, you're not checking to see if the input string is empty. This will cause a segmentation fault when you try to access a character at an index that doesn't exist. You should add a check for this at the beginning of your function.

In your truncate_number function, you're using the math.h library, which is unnecessary. You can just use the fmod function to get the fractional part of a floating point number.

In your get_row function, you're not sorting the coordinates in the way that the problem statement specifies. You should be sorting the coordinates of each row by columns in descending order, but you're currently sorting them in ascending order. You can use the sort function from the algorithm library to sort the coordinates.

Here's a corrected version of your get_row function:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<vector<int>> get_row(vector<vector<int>> lst, int x){

    vector<vector<int>> all_x;
    int i,j;
    for (i=0;i<lst.size();i++)
    for (j=0;j<lst[i].size();j++)
    if (lst[i][j]==x)
    {
        vector<int> temp={i,j};
        all_x.push_back(temp);
    }
    for (i=0;i<all_x.size();i++)
    {
        sort(all_x[i].begin(), all_x[i].end(), greater<int>());
    }
    return all_x;
}