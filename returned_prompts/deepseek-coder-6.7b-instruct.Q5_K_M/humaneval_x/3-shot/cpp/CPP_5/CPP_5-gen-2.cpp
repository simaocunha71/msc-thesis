    for(int i=0; i<numbers.size()*2-1; i+=2){
        numbers.insert(numbers.begin()+i+1, delimeter);
    }
    return numbers;
}

