    vector<int> result;
    sort(arr.begin(),arr.end());
    int i = 0;
    while(k--){
        result.push_back(arr[i++]);
    }
    return result;

B:
    //B:
    vector<int> result(arr);
    sort(result.begin(),result.end());
    result.resize(k);
    return result;
}

C:
    //C:
    sort(arr.begin(),arr.end(),greater<int>());
    vector<int> result(arr.begin(),arr.begin()+k);
    return result;

D:
    //D:
    vector<int> result(k);
    sort(arr.begin(),arr.end());
    for(int i = 0;i < k;i++){
        result[i] = arr[arr.size()-i-1];
    }
    return result;
}

E:
    //E:
    vector<int> result(arr.begin(),arr.begin()+k);
    sort(result.begin(),result.end(),greater<int>());
    return result;

F:
    //F:
    vector<int> result(k);
    for(int i = 0;i < k;i++){
        result[i] = arr[arr.size()-i-1];
    }
    sort(result.begin(),result.end());
    return result;
}

G:
    //G:
    vector<int> result(k);
    sort(arr.begin(),arr.end());
    for(int i = 0;i < k;i++){
        result[i] = arr[arr.size()-i-1];
    }
    sort(result.begin(),result.end(),greater<int>());
    return result;
}

H:
    //H:
    vector<int> result(arr.begin(),arr.begin()+k);
    sort(result.begin(),result.end());
    sort(result.begin(),result.end(),greater<int>());
    return result;
}

I:
    //I:
    vector<int> result(k);
    for(int i = 0;i < k;i++){
        result[i] = arr[arr.size()-i-1];
    }
    sort(result.begin(),result.end(),greater<int>());
    return result;
}

J:
    //J:
    vector<int> result(k);
    sort(arr.begin(),arr.end());
    for(int i = 0;i < k;i++){
        result[i] = arr[i];
    }
    return result;
}

K:
    //K:
    vector<int> result(k);
    sort(arr.begin(),arr.end());
    for(int i = 0;i < k;i++){
        result[i] = arr[i];
    }
    sort(result.begin(),result.end(),greater<int