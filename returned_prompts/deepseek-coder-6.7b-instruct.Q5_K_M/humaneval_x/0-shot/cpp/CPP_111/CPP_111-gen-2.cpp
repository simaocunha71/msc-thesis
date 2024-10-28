    map<char,int> m;
    for(int i=0;i<test.size();i++){
        m[test[i]]++;
    }

    int max = 0;
    for(auto it = m.begin(); it != m.end(); it++){
        if(it->second > max){
            max = it->second;
        }
    }

    map<char,int> result;
    for(auto it = m.begin(); it != m.end(); it++){
        if(it->second == max){
            result[it->first] = it->second;
        }
    }
    return result;
}

int main(){
    printf("Hello World");
    return 0;
}

*/

/*
