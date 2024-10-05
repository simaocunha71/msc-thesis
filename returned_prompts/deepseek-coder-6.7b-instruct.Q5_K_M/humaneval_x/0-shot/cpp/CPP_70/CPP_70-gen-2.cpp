    sort(lst.begin(), lst.end());
    vector<int> res;
    while(!lst.empty()){
        res.push_back(lst.front());
        lst.erase(lst.begin());
        if(!lst.empty()){
            res.push_back(lst.back());
            lst.pop_back();
        }
    }
    return res;
}

int main(){
    vector<int> v = {1, 2, 3, 4};
    vector<int> r = strange_sort_list(v);
    for(int i = 0; i < r.size(); i++){
        printf("%d ", r[i]);
    }
    return 0;
}

This C++ code sorts the input vector in ascending order. It then creates a new vector that alternates between the smallest and largest remaining elements of the input vector, removing them as it goes. If the input vector has an even number of elements, it will start with the smallest, then the largest, then the next smallest, and so on. If the input vector has an odd number of elements, it will start with the smallest, then the largest, then the next smallest, and so on, except the last element, which will be left out.

The time complexity of this code is O(n log n) due to the sorting operation, where n is the