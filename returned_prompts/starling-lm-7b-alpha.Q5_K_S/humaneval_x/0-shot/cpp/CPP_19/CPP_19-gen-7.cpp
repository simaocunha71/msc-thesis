    map<string,int> m;
    m["zero"] = 0;
    m["one"] = 1;
    m["two"] = 2;
    m["three"] = 3;
    m["four"] = 4;
    m["five"] = 5;
    m["six"] = 6;
    m["seven"] = 7;
    m["eight"] = 8;
    m["nine"] = 9;

    string s = "";
    for(int i = 0; i < numbers.size(); ++i){
        if(numbers[i] >= '0' && numbers[i] <= '9'){
            s += numbers[i];
        }
    }

    int size = s.size();
    int a[size];
    for(int i = 0; i < size; ++i){
        a[i] = m[s.substr(i, 1)];
    }

    for(int i = 0; i < size; ++i){
        for(int j = i + 1; j < size; ++j){
            if(a[i] > a[j]){
                int tmp = a[i];
                a[i] = a[j];
                a[j] = tmp;
            }
        }
    }

    for(int i = 0; i < size; ++i){
        if(a[i] == 0){
            s = s.replace(i, 1, "zero");
        }else if(a[i] == 1){
            s = s.replace(i, 1, "one");
        }else if(a[i] == 2){
            s = s.replace(i, 1, "two");
        }else if(a[i] == 3){
            s = s.replace(i, 1, "three");
        }else if(a[i] == 4){
            s = s.replace(i, 1, "four");
        }else if(a[i] == 5){
            s = s.replace(i, 