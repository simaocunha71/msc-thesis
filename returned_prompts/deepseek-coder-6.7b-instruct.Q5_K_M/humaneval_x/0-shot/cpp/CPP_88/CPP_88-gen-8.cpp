    vector<int> sorted_array = array;
    sort(sorted_array.begin(), sorted_array.end());
    if ((sorted_array.front() + sorted_array.back()) % 2 == 0)
        reverse(sorted_array.begin(), sorted_array.end());

    return sorted_array;
}

int main(){
    vector<int> array = {2, 4, 3, 0, 1, 5};
    vector<int> result = sort_array(array);
    for(auto i: result){
        printf("%d ", i);
    }
    return 0;
}

*/

*/
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> sort_array(vector<int> array){
    vector<int> sorted_array = array;
    sort(sorted_array.begin(), sorted_array.end());
    if ((sorted_array.front() + sorted_array.back()) % 2 == 0)
        reverse(sorted_array.begin(), sorted_array.end());

    return sorted_array;
}

int main(){
    vector<int> array = {2, 4, 3, 0, 1, 5};
    vector<int> result = sort_array(array);
    for(auto i: result){
        printf("%d ", i);
    }
    return 0;
}

/*
