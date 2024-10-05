    int i = 0;
    while(i<dict.size()){
        if(dict.begin()->first[0]>='A'&&dict.begin()->first[0]<='Z'){
            return false;
        }
        if(dict.begin()->first[0]>='a'&&dict.begin()->first[0]<='z'){
            dict.begin()->first=dict.begin()->first;
        }
        if(dict.begin()->second[0]>='A'&&dict.begin()->second[0]<='Z'){
            return false;
        }
        if(dict.begin()->second[0]>='a'&&dict.begin()->second[0]<='z'){
            dict.begin()->second=dict.begin()->second;
        }
        i++;
    }
    return true;
}
int main(){
    map<string,string> dict;
    dict.insert(pair<string,string>("a","apple"));
    dict.insert(pair<string,string>("A","banana"));
    dict.insert(pair<string,string>("B","banana"));
    dict.insert(pair<string,string>("8","banana"));
    dict.insert(pair<string,string>("STATE","NC"));
    dict.insert(pair<string,string>("ZIP","12345"));
    printf("%d\n",check_dict_case(dict));
    return 0;
}

*/








































































































































































