    return str.length();
}
// alternative solution
int strlen(string str){
    int count = 0;
    for(int i = 0; i < str.length(); i++){
        count++;
    }
    return count;
}