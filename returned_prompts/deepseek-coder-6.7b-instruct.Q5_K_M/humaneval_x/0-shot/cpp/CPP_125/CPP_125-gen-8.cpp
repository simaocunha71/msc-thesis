vector<string> res;
string word;
for(char c : txt){
    if(c == ' ' || c == ','){
        if(!word.empty()){
            res.push_back(word);
            word.clear();
        }
    }
    else{
        word += c;
    }
}
if(!word.empty()){
    res.push_back(word);
}
if(res.empty()){
    int count = 0;
    for(char c : txt){
        if(islower(c) && ((c - 'a') % 2 == 1))
            count++;
    }
    res.push_back(to_string(count));
}
return res;
}
int main()
{
vector<string> v = split_words("Hello,world!");
for(auto s : v)
    printf("%s\n",s.c_str());
return 0;
}
*/

