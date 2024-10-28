    sort(lst.begin(), lst.end());
    vector<int> ret;
    while(!lst.empty()){
        ret.push_back(lst.front());
        lst.erase(lst.begin());
        if(!lst.empty()){
            ret.push_back(lst.back());
            lst.pop_back();
        }
    }
    return ret;
}

int main(){
    vector<int> v1{1, 2, 3, 4};
    vector<int> v2{5, 5, 5, 5};
    vector<int> v3{};
    vector<int> r1 = strange_sort_list(v1);
    vector<int> r2 = strange_sort_list(v2);
    vector<int> r3 = strange_sort_list(v3);
    for(int i = 0; i < r1.size(); i++) printf("%d ", r1[i]);
    printf("\n");
    for(int i = 0; i < r2.size(); i++) printf("%d ", r2[i]);
    printf("\n");
    for(int i = 0; i < r3.size(); i++) printf("%d ", r3[i]);
    printf("\n");
    return 0;
}

*/


// -----------------------------------------


/*

