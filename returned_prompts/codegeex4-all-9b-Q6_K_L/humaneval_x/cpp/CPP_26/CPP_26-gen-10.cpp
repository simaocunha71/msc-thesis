    for (int i=0;i<numbers.size();i++){
        for(int j=i+1;j<numbers.size();j++){
            if(numbers[i]==numbers[j]){
                numbers.erase(numbers.begin()+j);
                j--;
            }
        }
    }
    return numbers;
}

B:
    sort(numbers.begin(),numbers.end());
    numbers.erase(unique(numbers.begin(),numbers.end()),numbers.end());
    return numbers;
}

C:
    for (int i=0;i<numbers.size();i++){
        for(int j=numbers.size()-1;j>i;j--){
            if(numbers[i]==numbers[j]){
                numbers.erase(numbers.begin()+j);
            }
        }
    }
    return numbers;
}

D:
    vector<int> new_numbers;
    for(int i=0;i<numbers.size();i++){
        int count=0;
        for(int j=0;j<numbers.size();j++){
            if(numbers[i]==numbers[j]) count++;
        }
        if(count==1) new_numbers.push_back(numbers[i]);
    }
    return new_numbers;
}

E:
    for (int i=0;i<numbers.size();i++){
        for(int j=0;j<numbers.size();j++){
            if(numbers[i]==numbers[j]){
                numbers.erase(numbers.begin()+j);
                j--;
            }
        }
    }
    return numbers;
}

F:
    for(int i=0;i<numbers.size();i++){
        int count=0;
        for(int j=0;j<numbers.size();j++){
            if(numbers[i]==numbers[j]) count++;
        }
        if(count>1){
            numbers.erase(numbers.begin()+i);
            i--;
        }
    }
    return numbers;
}

G:
    vector<int> new_numbers;
    int count=0;
    for(int i=0;i<numbers.size();i++){
        for(int j=0;j<numbers.size();j++){
            if(numbers[i]==numbers[j]){
                count++;
            }
            if(count==1){
                new_numbers.push_back(numbers[i]);
            }
        }
    }
    return new_numbers;
}
