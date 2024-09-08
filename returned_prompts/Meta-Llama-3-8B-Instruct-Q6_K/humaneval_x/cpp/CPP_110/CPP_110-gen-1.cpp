    // Initialize a flag to track if it's possible to make all elements in lst1 even.
    bool possible = true;

    // Iterate over each element in lst1.
    for (int i = 0; i < lst1.size(); i++) {
        // If lst1[i] is not even, set the flag to false.
        if (lst1[i] % 2 != 0) {
            possible = false;
            break;
        }
    }

    // If it's not possible to make all elements in lst1 even, return "NO".
    if (!possible) {
        return "NO";
    }

    // Iterate over each element in lst2.
    for (int i = 0; i < lst2.size(); i++) {
        // If lst2[i] is even, find the first index j in lst1 where lst1[j] is not even.
        for (int j = 0; j < lst1.size(); j++) {
            if (lst1[j] % 2 != 0) {
                // Perform the exchange.
                int temp = lst1[j];
                lst1[j] = lst2[i];
                lst2[i] = temp;
                break;
            }
        }
    }

    // If all elements in lst1 are even after the exchange, return "YES".
    for (int i = 0; i < lst1.size(); i++) {
        if (lst1[i] % 2 != 0) {
            return "NO";
        }
    }

    return "YES";
}
int main() {
    vector<int> lst1 = {1, 2, 3, 4};
    vector<int> lst2 = {1, 2, 3, 4};
    cout << exchange(lst1, lst2) << endl; // Output: YES
    return 0;
}
B:
    #include <iostream>
    #include <vector>
    #include <string>
    using namespace std;

    string exchange(vector<int> lst1, vector<int> lst2) {
        // Check if all elements in lst1 are even
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1[i] % 2 != 0) {
                return "NO";
            }
        }

        // If all elements in lst1 are even, check if there are any odd numbers in lst2
        for (