    sort(lst.begin(), lst.end());
    vector<int> result;
    while(!lst.empty()){
        result.push_back(lst.front());
        lst.erase(lst.begin());
        if(!lst.empty()){
            result.push_back(lst.back());
            lst.pop_back();
        }
    }
    return result;
}

int main(){
    vector<int> v = {1, 2, 3, 4};
    vector<int> r = strange_sort_list(v);
    for(int i : r) printf("%d ", i);
    return 0;
}

Explanation:

The problem is about sorting an array in a strange order:
Starting with the smallest number, then the largest number, then the next smallest, and so on.

The solution is to sort the array and then repeatedly remove the smallest and largest elements and add them to the result.

The C++ code does exactly this. It uses the STL's sort function to sort the vector, and then uses a while loop to repeatedly remove the smallest and largest elements from the vector and add them to a new vector.
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> strange_sort_vector(vector<int> vec) {
    vector<int> result;
    sort(vec.begin(), vec.end());
    while (!vec.empty()) {
        result.push_back(vec.front());
        vec.erase(vec.begin());
        if (!vec.empty()) {
            result.push_back(vec.back());
            vec.pop_back();
        }
    }
    return result;
}

int main() {
    vector<int> v = {1, 2, 3, 4};
    vector<int> result = strange_sort_vector(v);
    for (int i : result) {
        cout << i << " ";
    }
    return 0;
}

