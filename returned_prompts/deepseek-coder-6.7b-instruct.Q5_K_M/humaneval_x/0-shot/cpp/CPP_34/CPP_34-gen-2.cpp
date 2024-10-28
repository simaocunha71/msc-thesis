    sort(l.begin(), l.end());
    l.erase(unique(l.begin(), l.end()), l.end());
    return l;
}

int main(){
    vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    l = unique(l);
    for(int i=0; i<l.size(); i++)
        printf("%d ", l[i]);
    return 0;
}

This program will print the sorted unique elements of the given vector. It uses the STL function `unique()` which removes the duplicate elements in the range [first, last) and returns a pointer to the new logical end of the range. The `sort()` function sorts the elements in the range [first, last) in ascending order. The program then returns the sorted vector with unique elements.

Note: The `unique()` function returns an iterator pointing to the new logical end of the range, and `erase()` function removes the elements from the vector that are beyond this new logical end.
*/

#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> unique(std::vector<int>& l) {
    std::sort(l.begin(), l.end());
    l.erase(std::unique(l.begin(), l.end()), l.end());
    return l;
}

int main() {
    std::vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    l = unique(l);
    for(int i=0; i<l.size(); i++)
        std::cout << l[i] << " ";
    return 0;
}

/*
This program will print the sorted unique elements of the given vector. It uses the STL function `std::unique()` which removes the duplicate elements in the range [first, last) and returns a pointer to the new logical end of the range. The `std::sort()` function sorts the elements in the range [first, last) in ascending order