    for(int i = numbers.size()*2-1; i > 0; i-=2)
    {
        numbers.insert(numbers.begin()+i, delimeter);
    }
    return numbers; 
}


