    for(auto a:dict){
        if(a.first[0]>=65&&a.first[0]<=90||a.first[0]>=97&&a.first[0]<=122){
            if(a.second[0]>=97&&a.second[0]<=122||a.second[0]>=65&&a.second[0]<=90){
                continue;
            }else{
                return false;
            }
        }else{
            return false;
        }
    }
    return true;
}

int main()
{
    map<string,string> dict;
    dict[string("a")]=string("apple");
    dict[string("A")]=string("banana");
    dict[string("B")]=string("banana");
    dict[string("STATE")]=string("NC");
    dict[string("ZIP")]=string("12345");
    if(check_dict_case(dict)){
        printf("true");
    }else{
        printf("false");
    }
    return 0;
}

*/















































































































































































































































