    for(int i = 0; i < l.size(); i++){
        l[i] += 1;
    }
    return l;
}

int main(){
    vector<int> v = {1, 2, 3};
    v = incr_list(v);
    for(int i = 0; i < v.size(); i++){
        printf("%d ", v[i]);
    }
    return 0;
}

Output:
2 3 4 


A: Your function name and variable name "incr_list" are not matching. Also, the function should return vector not list.
You should change the function name to match with variable name and return type to vector.
Try this:
#include<iostream>
#include<vector>
using namespace std;

vector<int> incr_vector(vector<int> l){
    for(int i = 0; i < l.size(); i++){
        l[i] += 1;
    }
    return l;
}

int main(){
    vector<int> v = {1, 2, 3};
    v = incr_vector(v);
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
    return 0;
}

Output:
2 3 4


A: You're almost there, but there are a few things you need to fix:


*

*In your main function, you are trying to print the elements of a vector with printf. printf is used for printing formatted output, not for printing the elements of a vector. To print the elements of a vector in C++, you should use a range-based for loop or the function std::copy with std::ostream_iterator.

*Your function name is "incr_list" but you are trying to use "incr_vector". They should match.

*Your function name is "incr_list" but the return type is "vector<int>". They should match.


Here is the corrected code:
#include<iostream>
#include<vector>
using namespace std;
