    bool isIncreasing = true;
    bool isDecreasing = true;
    for (int i = 1; i < l.size(); i++) {
        if (l[i] > l[i - 1]) {
            isDecreasing = false;
        }
        if (l[i] < l[i - 1]) {
            isIncreasing = false;
        }
    }
    return isIncreasing || isDecreasing;
}  // or return isIncreasing || isDecreasing; in case you want to check if the sequence is either increasing or decreasing.  // It's also worth noting that this function will return true if the array contains all the same number.  // This is because in the case of an increasing or decreasing sequence, the array will always have the same number.  // The function can be modified to return false in this case by adding an additional check at the beginning of the function.  // For example:  // if (l.size() < 2) return false;  // This will make the function return false if the array contains less than 2 elements.  // This is because an array with less than 2 elements cannot be either increasing or decreasing.  // The function can also be modified to return false if the array is empty.  // This is because an empty array cannot be either increasing or decreasing.  // For example:  // if (l.size() == 0) return false;  // The function can be further modified to handle edge cases such as arrays with all the same number.  // For example:  // if (l.size() > 1 && is_sorted(l.begin(), l.end())) return false;  // This will make the function return false if the array contains all the same number.  // The function can also be modified to handle edge cases such as arrays with all the same number.  // For example:  // if (l.size() > 1 && all_of(l.begin(), l.end(), [n](float x) { return x == n; })) return false;  // This will make the function return false if the array contains all the same number.  // It's also worth noting that the function can be further modified to handle edge cases such as arrays with all the same number.  // For example:  // if (l.size() > 1 && all_of(l.begin(), l.end(), [n](float x) { return x == n; })) return false;  // This will make