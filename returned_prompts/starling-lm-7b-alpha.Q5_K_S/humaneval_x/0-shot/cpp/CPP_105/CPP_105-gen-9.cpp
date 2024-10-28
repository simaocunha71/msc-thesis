    vector<int> tmp;
    int num = 0;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] > 0 && arr[i] < 10) {
            tmp.push_back(arr[i]);
        }
    }
    sort(tmp.begin(), tmp.end());
    reverse(tmp.begin(), tmp.end());
    vector<string> ret;
    for (int i = 0; i < tmp.size(); i++) {
        switch (tmp[i]) {
            case 1: ret.push_back("One"); break;
            case 2: ret.push_back("Two"); break;
            case 3: ret.push_back("Three"); break;
            case 4: ret.push_back("Four"); break;
            case 5: ret.push_back("Five"); break;
            case 6: ret.push_back("Six"); break;
            case 7: ret.push_back("Seven"); break;
            case 8: ret.push_back("Eight"); break;
            case 9: ret.push_back("Nine"); break;
            default: break;
        }
    }
    return ret;
}
int main() {
    vector<int> arr;
    vector<string> res;
    int tmp;
    while (scanf("%d", &tmp) != EOF) {
        arr.push_back(tmp);
    }
    res = by_length(arr);
    for (int i = 0; i < res.size(); i++) {
        printf("%s ", res[i].c_str());
    }
    printf("\n");
    return 0;
}




























































































