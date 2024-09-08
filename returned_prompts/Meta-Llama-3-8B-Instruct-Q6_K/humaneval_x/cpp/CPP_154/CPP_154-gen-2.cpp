    int len_a = a.length();
    int len_b = b.length();
    for(int i = 0 ; i < len_a ; i++){
        string temp = a.substr(i,len_a);
        if(temp.find(b) != string::npos){
            return true;
        }
    }
    for(int i = 0 ; i < len_b ; i++){
        string temp = b.substr(i,len_b);
        if(a.find(temp) != string::npos){
            return true;
        }
    }
    return false;
}
int main(){
    cout<<cycpattern_check("abcd","abd")<<endl;
    cout<<cycpattern_check("hello","ell")<<endl;
    cout<<cycpattern_check("whassup","psus")<<endl;
    cout<<cycpattern_check("abab","baa")<<endl;
    cout<<cycpattern_check("efef","eeff")<<endl;
    cout<<cycpattern_check("himenss",'simen')<<endl;
    return 0;
}
