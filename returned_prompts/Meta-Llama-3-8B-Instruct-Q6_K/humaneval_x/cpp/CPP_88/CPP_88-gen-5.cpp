    int sum = 0;
    sum += array[0];
    sum += array[array.size() - 1];

    if(sum % 2 == 0){
        sort(array.begin(), array.end(), greater<int>());
    }else{
        sort(array.begin(), array.end());
    }
    return array;
}

