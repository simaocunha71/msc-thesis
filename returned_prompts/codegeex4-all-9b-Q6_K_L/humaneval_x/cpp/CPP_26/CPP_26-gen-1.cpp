for(int i=0;i<numbers.size();i++){
    for(int j=i+1;j<numbers.size();j++){
        if(numbers[i]==numbers[j]){
            numbers.erase(numbers.begin()+j);
        }
    }
}
    return numbers;
}

B:
for(int i=0;i<numbers.size();i++){
    for(int j=i+1;j<numbers.size();j++){
        if(numbers[i]==numbers[j]){
            numbers.erase(numbers.begin()+j);
            j--;
        }
    }
}
    return numbers;

C:
sort(numbers.begin(),numbers.end());
for(int i=1;i<numbers.size();i++){
    if(numbers[i]==numbers[i-1]){
        numbers.erase(numbers.begin()+i);
        i--;
    }
}
    return numbers;

D:
for(int i=0;i<numbers.size();i++){
    for(int j=i+1;j<numbers.size();j++){
        if(numbers[i]==numbers[j]){
            numbers.erase(numbers.begin()+j);
            j--;
        }
    }
}
    sort(numbers.begin(),numbers.end());
    return numbers;

E:
sort(numbers.begin(),numbers.end());
for(int i=0;i<numbers.size();i++){
    for(int j=i+1;j<numbers.size();j++){
        if(numbers[i]==numbers[j]){
            numbers.erase(numbers.begin()+j);
        }
    }
}
    return numbers;

F:
for(int i=0;i<numbers.size();i++){
    for(int j=i+1;j<numbers.size();j++){
        if(numbers[i]==numbers[j]){
            numbers.erase(numbers.begin()+j);
            j--;
        }
    }
}
    sort(numbers.begin(),numbers.end());
    numbers.erase(unique(numbers.begin(),numbers.end()),numbers.end());
    return numbers;

G:
sort(numbers.begin(),numbers.end());
numbers.erase(unique(numbers.begin(),numbers.end()),numbers.end());
    return numbers;

H:
for(int i=0;i<numbers.size();i++){
    for(int j=i+1;j<numbers.size();j++){
        if(numbers[i]==numbers[j]){
            numbers.erase(numbers.begin()+j);
            j--;
        }
    }
}
    sort(numbers.begin(),numbers.end());
    numbers.erase(unique(numbers.begin(),numbers.end()),numbers.end());
    return numbers;

I:
numbers.erase(unique(numbers.begin(),numbers.end()),numbers.end());
    return numbers;

J:
for(int i=0;i<numbers.size();i++){
    for(int j=i+1;j<numbers.size();j++){
        if(numbers[i]==numbers