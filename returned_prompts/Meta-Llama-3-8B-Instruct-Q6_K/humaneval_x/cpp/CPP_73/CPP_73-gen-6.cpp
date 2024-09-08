    // calculate the length of the vector
    int n = arr.size();

    // create a copy of the vector
    vector<int> arr_copy = arr;

    // sort the copy of the vector
    sort(arr_copy.begin(), arr_copy.end());

    // create a map to store the frequency of each element
    map<int, int> freq;

    // calculate the frequency of each element in the sorted vector
    for (int i = 0; i < n; i++) {
        freq[arr_copy[i]]++;
    }

    // initialize the count of changes
    int changes = 0;

    // iterate over the original vector
    for (int i = 0; i < n; i++) {
        // for each element in the original vector
        for (auto it = freq.begin(); it != freq.end(); ++it) {
            // if the element is not in the original vector
            if (arr[i] != it->first) {
                // decrement the frequency of the element
                it->second--;
                // if the frequency of the element becomes zero
                if (it->second == 0) {
                    // remove the element from the map
                    freq.erase(it);
                }
                // increment the count of changes
                changes++;
                // break the inner loop
                break;
            }
        }
    }

    // return the count of changes
    return changes;
}

int main() {
    vector<int> arr = {1,2,3,5,4,7,9,6};
    printf("Minimum changes: %d\n", smallest_change(arr));
    return 0;
}

B:
    int smallest_change(std::vector<int> arr) {
        int n = arr.size();
        std::vector<int> arr_copy = arr;
        std::sort(arr_copy.begin(), arr_copy.end());
        std::map<int, int> freq;
        for (int i = 0; i < n; i++) {
            freq[arr_copy[i]]++;
        }
        int changes = 0;
        for (int i = 0; i < n; i++) {
            for (auto it = freq.begin(); it != freq.end(); ++it) {
                if (arr[i] != it->first) {
                    it->second--;
                    if (it->second == 0) {
                        freq.erase(it);
                    }
                    changes++;
                    break;
                }
            }
        }
        return changes