    int oddLst1=0, oddLst2=0;
    for(int i=0; i<lst1.size(); i++){
        if(lst1[i]%2 != 0)
            oddLst1++;
    }
    for(int i=0; i<lst2.size(); i++){
        if(lst2[i]%2 != 0)
            oddLst2++;
    }
    if(oddLst1 > oddLst2)
        return "NO";
    else
        return "YES";
}

int main() {
    vector<int> lst1{1, 2, 3, 4};
    vector<int> lst2{1, 2, 3, 4};
    printf("%s\n", exchange(lst1, lst2).c_str());

    vector<int> l