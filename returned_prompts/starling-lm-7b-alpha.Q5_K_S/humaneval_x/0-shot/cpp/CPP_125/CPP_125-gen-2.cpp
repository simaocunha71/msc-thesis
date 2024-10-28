    int i = 0;
    int j = 0;
    int k = 0;
    int z = 0;
    int l = txt.length();
    vector<string> ans;
    while(i < l){
        if(txt[i] == ',' || txt[i] == ' '){
            if(k != 0){
                ans.push_back(txt.substr(j, k));
            }
            j = i + 1;
            k = 0;
        }
        else{
            k++;
        }
        i++;
    }
    if(k != 0){
        ans.push_back(txt.substr(j, k));
    }
    return ans;
}

B:
    int i = 0;
    int j = 0;
    int k = 0;
    int z = 0;
    int l = txt.length();
    vector<int> ans;
    while(i < l){
        if(txt[i] == ',' || txt[i] == ' '){
            if(k != 0){
                ans.push_back(k);
            }
            j = i + 1;
            k = 0;
        }
        else{
            k++;
        }
        i++;
    }
    if(k != 0){
        ans.push_back(k);
    }
    return ans;
}

C:
    int i = 0;
    int j = 0;
    int k = 0;
    int z = 0;
    int l = txt.length();
    while(i < l){
        if(txt[i] == ',' || txt[i] == ' '){
            j = i + 1;
            k = 0;
        }
        else{
            k++;
        }
        i++;
    }
    if(k != 0){
        ans.push_back(k);
    }
    return ans;
}

























