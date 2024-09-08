    // Check if the vector is balanced
    string str = "";
    for(int i:q){
        str += to_string(i);
    }
    if(str != string(str.rbegin(), str.rend())){
        return false;
    }

    // Check if the sum of the vector is less than or equal to w
    int sum = 0;
    for(int i:q){
        sum += i;
    }
    if(sum > w){
        return false;
    }
    return true;
}

