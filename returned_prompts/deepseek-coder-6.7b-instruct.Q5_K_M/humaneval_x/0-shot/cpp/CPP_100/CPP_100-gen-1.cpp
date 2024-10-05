    vector<int> result;
    for(int i=0; i<n; i++){
        result.push_back(n + 2 * i);
    }
    return result;
}

int main(){
    int n;
    scanf("%d",&n);
    vector<int> result = make_a_pile(n);
    for(int i = 0; i < result.size(); i++)
        printf("%d ", result[i]);
    return 0;
}

*/

#include <iostream>
#include <vector>
using namespace std;

vector<int> make_a_pile(int n){
    vector<int> result;
    for(int i=0; i<n; i++){
        if(n%2 == 0)
            result.push_back(n + 2 * i);
        else
            result.push_back(n + 2 * i);
    }
    return result;
}

int main(){
    int n;
    cin >> n;
    vector<int> result = make_a_pile(n);
    for(int i = 0; i < result.size(); i++)
        cout << result[i] << " ";
    return 0;
}
/*
E:

The task is to create a vector of integers representing the number of stones in each level of the pile. 

First, we initialize an empty vector. Then, we loop through n times. In each iteration, we add the next odd number to the vector.

The number of stones in the next level is calculated as n + 2 * i, where i is the current level (starting from 0).

Finally, we return the vector.

This solution works for both even and odd n.

The time complexity of this solution is O(n), as we are looping through n levels of stones. The space complexity is also O(n), as we are storing n elements in the vector.
*/

// 01518-1
// 01518-2
// 01518-3
// 01518-4
// 01518