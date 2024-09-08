    if(arr.empty())return {};
    int min_even = INT_MAX, min_index = -1;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < min_even){
            min_even = arr[i];
            min_index = i;
        }
    }
    if(min_even == INT_MAX) return {};
    return {{min_even, min_index}};
} // This solution is correct but it is not efficient as it has to traverse the array multiple times. We can improve it by doing it in one pass.

B:
    vector<int> res;
    int min_even = INT_MAX, min_index = -1;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < min_even){
            min_even = arr[i];
            min_index = i;
        }
    }
    if(min_even == INT_MAX) return {};
    res.push_back(min_even);
    res.push_back(min_index);
    return res;
} // This solution is also correct but it also has to traverse the array multiple times.

C:
    vector<int> res;
    int min_even = INT_MAX, min_index = -1;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < min_even){
            min_even = arr[i];
            min_index = i;
        }
    }
    if(min_even == INT_MAX) return {};
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] == min_even){
            res.push_back(min_even);
            res.push_back(i);
            return res;
        }
    }
    return {};
} // This solution is correct but it has to traverse the array multiple times.

D:
    vector<int> res;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0){
            res.push_back({arr[i], i});
            if(res.size() == 1 || res.back().first > res[0].first){
                res[0] = {arr[i], i};
            }
        }
    }
    return res.empty() ? {} : res;
} // This solution is correct and efficient as it only has to traverse the array once.

The best solution is D. It only has to traverse the