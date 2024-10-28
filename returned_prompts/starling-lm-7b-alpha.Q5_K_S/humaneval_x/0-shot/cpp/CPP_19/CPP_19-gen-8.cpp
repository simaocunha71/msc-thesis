    map<string,int> mp;
    mp["zero"] = 0;
    mp["one"] = 1;
    mp["two"] = 2;
    mp["three"] = 3;
    mp["four"] = 4;
    mp["five"] = 5;
    mp["six"] = 6;
    mp["seven"] = 7;
    mp["eight"] = 8;
    mp["nine"] = 9;
    string res = "";
    for(int i=0;i<numbers.size();++i){
        if(numbers[i] == ' '){
            int a,b;
            if(res.size()){
                a = mp[res];
                res = "";
            }else{
                a = mp[numbers.substr(0,i)];
                numbers = numbers.substr(i+1);
            }
            if(numbers.size()){
                b = mp[numbers];
                numbers = "";
            }else{
                b = mp[res];
                res = "";
            }
            if(a < b){
                res = res + " " + numbers.substr(i-1,1);
            }else{
                res = res + " " + res.substr(i-1,1);
                res = res + " " + numbers.substr(i-1,1);
            }
        }
    }
    if(res.size()){
        res = res + " " + numbers;
    }else{
        res = res + " " + res;
        res = res + " " + numbers;
    }
    return res;
}

int main()
{
    printf("%s\n",sort_numbers("three one five").c_str());
    return 0;
}




























*/








































