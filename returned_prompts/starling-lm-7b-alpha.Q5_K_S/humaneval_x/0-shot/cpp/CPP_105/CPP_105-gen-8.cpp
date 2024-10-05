    sort(arr.begin(), arr.end());
    vector<int> tmp;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] > 0 && arr[i] < 10){
            tmp.push_back(arr[i]);
        }
    }
    sort(tmp.begin(), tmp.end());
    reverse(tmp.begin(), tmp.end());
    vector<string> ret;
    ret.push_back("One");
    ret.push_back("Two");
    ret.push_back("Three");
    ret.push_back("Four");
    ret.push_back("Five");
    ret.push_back("Six");
    ret.push_back("Seven");
    ret.push_back("Eight");
    ret.push_back("Nine");
    for(int i = 0; i < tmp.size(); i++){
        ret.push_back(ret[tmp[i]]);
    }
    return ret;
}

int main(){
    int a[10] = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<int> tmp(a, a + 10);
    vector<string> ret = by_length(tmp);
    for(int i = 0; i < ret.size(); i++){
        printf("%s ", ret[i].c_str());
    }
    printf("\n");
    return 0;
}

*/
















































































































































