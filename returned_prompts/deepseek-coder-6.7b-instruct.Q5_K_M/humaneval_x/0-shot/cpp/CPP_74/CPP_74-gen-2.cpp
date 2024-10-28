    int sum1 = 0, sum2 = 0;
    for(string s : lst1) sum1 += s.length();
    for(string s : lst2) sum2 += s.length();
    return sum1 < sum2 ? lst1 : lst2;
}

int main(){
    vector<string> lst1 = {"hi", "admin"};
    vector<string> lst2 = {"hI", "Hi"};
    vector<string> res = total_match(lst1, lst2);
    for(string s : res) printf("%s ", s.c_str());
    return 0;
}
