    sort(numbers.begin(),numbers.end());
    for(int i=0;i<numbers.size()-1;i++){
        if(numbers[i]==numbers[i+1]){
            numbers.erase(numbers.begin()+i);
            i--;
        }
    }
    return numbers;
}

B:
    sort(numbers.begin(),numbers.end());
    for(int i=0;i<numbers.size()-1;i++){
        if(numbers[i]==numbers[i+1]){
            numbers.pop_back();
        }
    }
    return numbers;
}

C:
    sort(numbers.begin(),numbers.end());
    int i=0;
    while(i<numbers.size()){
        if(numbers[i]==numbers[i+1]){
            numbers.erase(numbers.begin()+i);
        }
        else{
            i++;
        }
    }
    return numbers;
}

D:
    sort(numbers.begin(),numbers.end());
    vector<int> temp;
    for(int i=0;i<numbers.size()-1;i++){
        if(numbers[i]!=numbers[i+1]){
            temp.push_back(numbers[i]);
        }
    }
    return temp;
}

E:
    sort(numbers.begin(),numbers.end());
    for(int i=0;i<numbers.size()-1;i++){
        if(numbers[i]==numbers[i+1]){
            numbers.erase(numbers.begin()+i);
            i--;
        }
        else{
            i++;
        }
    }
    return numbers;
}
