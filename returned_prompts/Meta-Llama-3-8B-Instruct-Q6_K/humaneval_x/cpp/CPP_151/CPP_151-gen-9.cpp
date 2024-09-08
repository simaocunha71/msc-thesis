    long long sum = 0;
    for(auto i : lst){
        if(i > 0 && i == static_cast<int>(i)){
            sum += pow(i, 2);
        }
    }
    return sum;
}

