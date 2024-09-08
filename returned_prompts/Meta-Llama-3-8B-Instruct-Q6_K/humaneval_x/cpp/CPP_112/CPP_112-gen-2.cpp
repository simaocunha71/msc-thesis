    vector<string> result;
    string temp = s;
    for(int i = 0 ; i < c.length() ; i++){
        temp.erase(remove(temp.begin(), temp.end(), c[i]), temp.end());
    }
    string temp2 = temp;
    reverse(temp2.begin(), temp2.end());
    if(temp == temp2)
        result.push_back(temp);
    else
        result.push_back(temp);
    result.push_back((temp == temp2)?"True":"False");
    return result;
}
int main(){
    string s = "abcdedcba";
    string c = "ab";
    vector<string> res = reverse_delete(s,c);
    for(int i = 0 ; i < res.size() ; i++){
        printf("%s\n",res[i].c_str());
    }
    return 0;
}
