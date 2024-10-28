    string result;
    for (string s : strings){
        result += s;
    }
    return result;
}

int main(){
    vector<string> v1 = {};
    printf("%s\n", concatenate(v1).c_str());
    vector<string> v2 = {"a", "b", "c"};
    printf("%s\n", concatenate(v2).c_str());
    return 0;
}

*/

The C++ version of this code:

/*
