    vector<string> res;
    for(auto &str : lst){
        int count = 0;
        for(char &c : str){
            if((c-'0') % 2 != 0) count++;
        }
        string temp = "the number of odd elements in the string "+to_string(count)+" of the input.";
        res.push_back(temp);
    }
    return res;
}
int main(){
    vector<string> v = {"3","11111111"};
    vector<string> res = odd_count(v);
    for(auto &s : res){
        printf("%s\n", s.c_str());
    }
    return 0;
}
*/

//