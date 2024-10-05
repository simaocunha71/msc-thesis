    for (int i=0;i<b.size();i++){
        string temp=b.substr(i)+b.substr(0,i);
B:
        if(a.find(temp)!=string::npos){
            return true;
        }
    }
    return false;
}
int main(){
    printf(cycpattern_check("abcd","abd")? "true" : "false"); //false
    printf(cycpattern_check("hello","ell")? "true" : "false"); //true
    printf(cycpattern_check("whassup","psus")? "true" : "false"); //false
    printf(cycpattern_check("abab","baa")? "true" : "false"); //true
    printf(cycpattern_check("efef","eeff")? "true" : "false"); //false
    printf(cycpattern_check("himenss",'simen')? "true" : "false"); //true
    return 0;
}

*/

