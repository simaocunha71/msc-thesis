    vector<int> result;
    if(lst.empty()) {
        return result;
    }

    sort(lst.begin(), lst.end());
    result.push_back(lst[0]);
    lst.erase(lst.begin());
    sort(lst.begin(), lst.end(), greater<int>());
    result.push_back(lst[0]);
    lst.erase(lst.begin());
    while(!lst.empty()) {
        result.push_back(lst[0]);
        lst.erase(lst.begin());
    }
    return result;
}

B:
    vector<int> strange_sort_list(vector<int> lst) {
        if(lst.empty()) {
            return vector<int>();
        }

        sort(lst.begin(), lst.end());
        vector<int> result;
        while(!lst.empty()) {
            result.push_back(lst[0]);
            lst.erase(lst.begin());
            if(!lst.empty()) {
                sort(lst.begin(), lst.end(), greater<int>());
                lst.erase(lst.begin());
            }
        }
        return result;
    }

C:
    vector<int> strange_sort_list(vector<int> lst) {
        if(lst.empty()) {
            return vector<int>();
        }

        sort(lst.begin(), lst.end());
        vector<int> result;
        result.push_back(lst[0]);
        lst.erase(lst.begin());
        sort(lst.begin(), lst.end(), greater<int>());
        while(!lst.empty()) {
            if(lst[0] < result.back()) {
                result.push_back(lst[0]);
            }
            lst.erase(lst.begin());
        }
        return result;
    }

D:
    vector<int> strange_sort_list(vector<int> lst) {
        if(lst.empty()) {
            return vector<int>();
        }

        sort(lst.begin(), lst.end());
        vector<int> result;
        result.push_back(lst[0]);
        lst.erase(lst.begin());
        sort(lst.begin(), lst.end(), greater<int>());
        while(!lst.empty()) {
            if(lst[0] < result.back()) {
                result.push_back(lst[0]);
            }
            lst.erase(lst.begin());
        }
        return result;
    }

E:
    vector<int> strange_sort_list(vector<int> lst) {
        if(lst.empty()) {
            return vector<int>();
        }

        sort(lst.begin(), lst.end());
        vector<int> result;
        result.push_back(lst[0]);
        lst.erase(lst.begin());
        sort(lst.begin(), lst.end(), greater<int>());
        while(!lst.empty()) {
            result.push_back(lst[0]);
            lst.erase(lst.begin());
        }
        return result;
    }

F:
    vector<int> strange_sort