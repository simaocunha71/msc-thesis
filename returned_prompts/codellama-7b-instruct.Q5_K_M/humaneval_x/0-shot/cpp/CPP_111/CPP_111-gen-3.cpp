    map<char,int> result;
    int count = 0;
    for(int i = 0; i < test.length(); i++){
        if(test[i] == ' '){
            count = 0;
        }
        else{
            count++;
        }
        if(count > 0){
            result[test[i]] = count;
        }
    }
    return result;
}
int main(){
    histogram("a b c");
    return 0;
}

