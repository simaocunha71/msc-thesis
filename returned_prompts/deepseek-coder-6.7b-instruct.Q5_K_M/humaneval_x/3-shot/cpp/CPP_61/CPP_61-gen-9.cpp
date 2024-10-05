    int count = 0;
    for(auto& ch : brackets) {
        if(ch == '(') count++;
        if(ch == ')') count--;
        if(count < 0) return false;
    }
    return count == 0;
}


