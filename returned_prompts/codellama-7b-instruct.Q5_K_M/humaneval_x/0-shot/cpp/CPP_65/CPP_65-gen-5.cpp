    string temp = "";
    while(x > 0){
        temp += to_string(x%10);
        x /= 10;
    }
    for(int i = 0; i < shift; i++){
        temp.insert(temp.begin(), temp.back());
        temp.pop_back();
    }
    return temp;
}

