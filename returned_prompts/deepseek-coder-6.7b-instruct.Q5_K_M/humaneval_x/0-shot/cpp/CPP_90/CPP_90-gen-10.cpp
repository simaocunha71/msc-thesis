    if (lst.size()<2) return NULL;
    sort(lst.begin(), lst.end());
    for (int i=0; i<lst.size()-1; i++){
        if (lst[i]<lst[i+1]) return lst[i+1];
    }
    return NULL;
}

int main(){
    vector<int> vec1 = {1, 2, 3, 4, 5};
    vector<int> vec2 = {5, 1, 4, 3, 2};
    vector<int> vec3 = {};
    vector<int> vec4 = {1, 1};

    printf("%d\n", next_smallest(vec1)); // should print 2
    printf("%d\n", next_smallest(vec2)); // should print 2
    printf("%d\n", next_smallest(vec3)); // should print NULL (None in python)
    printf("%d\n", next_smallest(vec4)); // should print NULL (None in python)
    return 0;
}

*/

/*
I:

The problem is asking to sort the vector in ascending order and then find the second smallest element. If there is no such element, return None.

P:

The problem can be solved using the sort function in the C++ STL. This function will sort the given vector in ascending order. After sorting, we will find the second smallest element and return it. If there is no such element, we will return None.

E:

Here are some examples to help understand the problem better:

next_smallest({1, 2, 3, 4, 5}) → 2
next_smallest({5, 1, 4, 3, 2}) → 2
next_smallest({}) → None
next_smallest({1, 1}) → None

T:

We can solve this problem in O(n log n) time complexity because of the sorting. After sorting, finding the second smallest element takes O(n) time. So, the total time complexity is O(n log