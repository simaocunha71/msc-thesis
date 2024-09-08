    vector<int> result;
    int sum = 0;
    int product = 1;
    for(int number : numbers){
        sum += number;
        product *= number;
    }
    result.push_back(sum);
    result.push_back(product);
    return result;
}

B:
    vector<int> result;
    int sum = 0;
    int product = 1;
    for(int number : numbers){
        sum += number;
        product *= number;
    }
    result.push_back(sum);
    result.push_back(product);
    return result;
}

C:
    vector<int> result;
    int sum = 0;
    int product = 1;
    for(int number : numbers){
        if(numbers.empty()){
            result.push_back(0);
            result.push_back(1);
        }else{
            sum += number;
            product *= number;
        }
    }
    result.push_back(sum);
    result.push_back(product);
    return result;
}

D:
    vector<int> result;
    if(numbers.empty()){
        result.push_back(0);
        result.push_back(1);
    }else{
        int sum = 0;
        int product = 1;
        for(int number : numbers){
            sum += number;
            product *= number;
        }
        result.push_back(sum);
        result.push_back(product);
    }
    return result;E:

    vector<int> result;
    if(numbers.empty()){
        result.push_back(0);
        result.push_back(1);
    }else{
        int sum = 0;
        int product = 1;
        for(int number : numbers){
            sum += number;
            product *= number;
        }
        result.push_back(sum);
        result.push_back(product);
    }
    return result;
}
F:
    vector<int> result;
    if(numbers.empty()){
        result.push_back(0);
        result.push_back(1);
    }else{
        int sum = 0;
        int product = 1;
        for(int number : numbers){
            sum += number;
            product *= number;
        }
        result.push_back(sum);
        result.push_back(product);
    }
    return result;
}

G:
    vector<int> result;
    if(numbers.empty()){
        result.push_back(0);
        result.push_back(1);
    }else{
        int sum = 0;
        int product = 1;
        for(int number : numbers){
            sum += number;
            product *= number;
        }
        result.push