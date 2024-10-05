    vector<string>ans;
    if(txt.find(" ")!=string::npos)ans=split(txt," ");
    else if(txt.find(",")!=string::npos)ans=split(txt,",");
    else{
        for(int i=0;i<txt.size();i++)
            if(txt[i]>='a' && txt[i]<='z')ans.push_back(to_string(txt[i]-'a'));
    }
    return ans;
}
vector<string> split(string str, string delim) {
    vector<string> result;
    if (str.size() == 0) {
        return result;
    }
    while (str.size() > 0) {
        string tmp = "";
        size_t pos = 0;
        while ((pos = str.find(delim)) != string::npos) {
            tmp += str.substr(0, pos);
            str = str.substr(pos + delim.size());
        }
        tmp += str;
        str = "";
        result.push_back(tmp);
    }
    return result;
}
int main(){
    vector<string> ans=split_words("abcdef");
    for(int i=0;i<ans.size();i++)printf("%s\n",ans[i].c_str());
}























































































































































































