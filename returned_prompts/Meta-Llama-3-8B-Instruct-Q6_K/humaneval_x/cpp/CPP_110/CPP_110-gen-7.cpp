    // your code here
    vector<int> result;
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i]%2 != 0){
            for(int j = 0; j < lst2.size(); j++){
                if(lst2[j]%2 == 0){
                    lst1[i] = lst2[j];
                    result.push_back(lst2[j]);
                    break;
                }
            }
        }
    }
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i]%2 != 0){
            return "NO";
        }
    }
    return "YES";
}

int main() {
    vector<int> lst1 = {1, 2, 3, 4};
    vector<int> lst2 = {1, 2, 3, 4};
    string result = exchange(lst1, lst2);
    printf("%s\n", result.c_str());
    return 0;
}

B:
    // your code here
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i]%2 != 0){
            for(int j = 0; j < lst2.size(); j++){
                if(lst2[j]%2 == 0){
                    int temp = lst1[i];
                    lst1[i] = lst2[j];
                    lst2[j] = temp;
                    break;
                }
            }
        }
    }
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i]%2 != 0){
            return "NO";
        }
    }
    return "YES";
}

int main() {
    vector<int> lst1 = {1, 2, 3, 4};
    vector<int> lst2 = {1, 2, 3, 4};
    string result = exchange(lst1, lst2);
    printf("%s\n", result.c_str());
    return 0;
}

C:
    // your code here
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i]%2 != 0){
            for(int j = 0; j < lst2.size(); j++){
                if(lst2[j]%2 == 0){
                    swap(lst1[i], lst2[j]);
                    break;
                }
            }
        }
    }
    for(int i = 0; i < lst1.size