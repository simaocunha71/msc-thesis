
    string temp="";
    string temp1="";
    string temp2="";
    for(int i=0;i<a.size();i++){
        temp+=a[i];
    }
    for(int i=0;i<b.size();i++){
        temp1+=b[i];
    }
    for(int i=0;i<temp.size();i++){
        if(temp.find(temp1)==string::npos){
            continue;
        }
        else{
            return true;
        }
    }
    return false;
}

int main(){
    string a="abcde";
    string b="abd";
    cout<<cycpattern_check(a,b)<<endl;
    return 0;
}
