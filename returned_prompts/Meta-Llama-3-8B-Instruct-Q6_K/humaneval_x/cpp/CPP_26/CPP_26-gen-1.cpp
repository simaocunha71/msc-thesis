    vector<int> result;
    for(int i = 0; i < numbers.size(); i++){
        bool found = false;
        for(int j = 0; j < result.size(); j++){
            if(numbers[i] == result[j]){
                found = true;
                break;
            }
        }
        if(!found) result.push_back(numbers[i]);
    }
    return result;

B:
    vector<int> result;
    for(int i = 0; i < numbers.size(); i++){
        bool duplicate = false;
        for(int j = 0; j < i; j++){
            if(numbers[i] == result[j]){
                duplicate = true;
                break;
            }
        }
        if(!duplicate) result.push_back(numbers[i]);
    }
    return result;

C:
    vector<int> result;
    unordered_set<int> seen;
    for(int i = 0; i < numbers.size(); i++){
        if(seen.find(numbers[i]) == seen.end()) {
            result.push_back(numbers[i]);
            seen.insert(numbers[i]);
        }
    }
    return result;

D:
    vector<int> result;
    unordered_map<int, int> count;
    for(int i = 0; i < numbers.size(); i++){
        count[numbers[i]]++;
    }
    for(int i = 0; i < numbers.size(); i++){
        if(count[numbers[i]] == 1) result.push_back(numbers[i]);
    }
    return result;

}
int main() {
    vector<int> numbers = {1, 2, 3, 2, 4};
    vector<int> result = remove_duplicates(numbers);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}
*/



Explanation:
This C++ program removes duplicates from a given vector of integers. The function `remove_duplicates` takes a vector of integers as input and returns a new vector with duplicates removed.

A: The first approach iterates over the input vector and checks if each element is already present in the result vector. If not, it adds the element to the result vector. This approach has a time complexity of O(n^2) due to the nested loops.

B: The second approach is similar to the first one, but it only checks the elements before the current index. This approach also has a time complexity of O(n^2) due to the nested loops.

C: The third approach uses