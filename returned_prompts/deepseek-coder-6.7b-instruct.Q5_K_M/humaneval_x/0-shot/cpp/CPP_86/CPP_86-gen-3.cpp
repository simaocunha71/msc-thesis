    string result = "";
    string temp = "";
    for(int i=0; i<s.length(); i++){
        if(s[i] == ' '){
            sort(temp.begin(), temp.end());
            result += temp + " ";
            temp = "";
        }else{
            temp += s[i];
        }
    }
    sort(temp.begin(), temp.end());
    result += temp;
    return result;
}
int main(){
    printf("%s", anti_shuffle("Hello World!!!").c_str());
    return 0;
}
*/
/*
