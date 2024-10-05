    for(int i=arr.size()-1; i>0; i--){
        if(arr[i]<arr[i-1]){
            return i;
        }
    }
    return -1;
}

int main() {
    vector<int> arr = {1,2,4,3,5};
    printf("%d", can_arrange(arr));
    return 0;
}

Answer:
The function works by iterating through the array from the end (to satisfy the problem's requirement of finding the "last" index) and comparing each element to its previous one. If the current element is less than its predecessor, it returns the current index. If it doesn't find such an element after checking all of them, it returns -1.

The complexity of this solution is O(n), where n is the size of the input array. This is because in the worst case scenario, the function must iterate through all the elements of the array.

The solution uses the standard vector library in C++. The function can_arrange is declared to take a vector of integers and return an integer. The main function tests this function with a vector of integers, and prints the result.
*/

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes here

// Your code goes