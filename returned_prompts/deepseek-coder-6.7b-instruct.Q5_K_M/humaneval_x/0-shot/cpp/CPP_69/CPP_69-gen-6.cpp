    sort(lst.begin(), lst.end());

B:
    for (int i = lst.size()-1; i >= 0; i--) {
        int count = 0;
        int num = lst[i];
        for (int j = 0; j < lst.size(); j++) {
            if(lst[j] == num)
                count++;
        }
        if(count >= num)
            return num;
    }

C:
    return -1;
}

int main() {
    vector<int> lst = {4,1,2,2,3,1};
    printf("%d ", search(lst));
    lst = {1,2,2,3,3,3,4,4,4};
    printf("%d ", search(lst));
    lst = {5,5,4,4,4};
    printf("%d ", search(lst));
    return 0;
}

*/

/*
The given C++ code is a solution to the problem statement. The code begins with sorting the input vector.
Then it starts from the end of the vector, counts the frequency of each number and checks if it's equal or
greater than the number itself. The first number that satisfies this condition is returned as the result. If no
such number is found, -1 is returned.
*/

// End of solution

// C++ Solution for Problem statement
/*
#include <iostream>
#include <vector>
#include <algorithm>

int search(std::vector<int> lst){
    std::sort(lst.begin(), lst.end());

    for (int i = lst.size()-1; i >= 0; i--) {
        int count = std::count(lst.begin(), lst.end(), lst[i]);
        if(count >= lst[i])
            return lst[i];
    }
    return -1;
}

int main() {
    std::vector<int> lst = {4,1,2,2,3,1};
    std::cout << search(lst) <<