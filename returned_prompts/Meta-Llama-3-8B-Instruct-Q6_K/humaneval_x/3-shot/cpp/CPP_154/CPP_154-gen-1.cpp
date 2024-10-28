    string temp = b;
    for(int i = 0; i < b.length(); i++){
        if(a.find(temp) != string::npos){
            return true;
        }
        temp = b.substr(1) + b[0];
    }
    return false;
}