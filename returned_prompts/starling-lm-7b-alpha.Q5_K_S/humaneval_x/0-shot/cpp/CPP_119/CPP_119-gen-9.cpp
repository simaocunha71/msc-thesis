    int n = lst.size();
    if(n == 0)
        return "No";
    if(n == 1){
        if(lst[0].find("(") != string::npos && lst[0].find(")") != string::npos)
            return "No";
        else
            return "Yes";
    }
    if(lst[0].find("(") != string::npos && lst[0].find(")") != string::npos){
        if(lst[1].find("(") != string::npos && lst[1].find(")") != string::npos){
            if(lst[0].length() != lst[1].length())
                goto A;
            else
                return "Yes";
        }
        else
            return "No";
    }
    else{
        if(lst[1].find("(") != string::npos && lst[1].find(")") != string::npos){
            if(lst[0].find("(") != string::npos && lst[0].find(")") != string::npos){
                if(lst[0].length() != lst[1].length())
                    goto A;
                else
                    return "Yes";
            }
            else
                return "No";
        }
        else
            return "No";
    }
}

int main(){
    vector<string> lst;
    lst.push_back("(");
    lst.push_back(")");
    lst.push_back("()");
    lst.push_back("()(");
    lst.push_back(")(()");
    lst.push_back("()())");
    lst.push_back("())");
    lst.push_back(")(");
    lst.push_back("(()");
    lst.push_back("))(");
    lst.push_back("))(");
    lst.push_back("()()(");
    lst.push_back("()(())");
    lst.push_back(")()