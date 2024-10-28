    // Sort the array
    sort(lst.begin(), lst.end());

    // Create a result vector
    vector<int> res;

    // While there are elements in the input list
    while(!lst.empty()) {
        // Take the smallest element
        res.push_back(lst.front());
        lst.erase(lst.begin());

        // If there are still elements in the input list
        if(!lst.empty()) {
            // Take the largest element
            res.push_back(lst.back());
            lst.pop_back();
        }
    }

    // Return the result
    return res;
}

int main() {
    vector<int> test1 = {1, 2, 3, 4};
    vector<int> test2 = {5, 5, 5, 5};
    vector<int>