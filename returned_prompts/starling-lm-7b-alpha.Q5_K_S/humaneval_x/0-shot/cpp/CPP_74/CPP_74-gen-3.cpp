    int lst1_sum=0,lst2_sum=0;
    for(int i=0;i<lst1.size();i++)
        lst1_sum+=lst1[i].length();
    for(int i=0;i<lst2.size();i++)
        lst2_sum+=lst2[i].length();
    if(lst1_sum<lst2_sum) return lst1;
    else if(lst1_sum>lst2_sum) return lst2;
    else {
        vector<string> same;
        for(int i=0;i<lst1.size();i++)
            same.push_back(lst1[i]);
        return same;
    }

}
int main(){
    vector<string> lst1,lst2;
    lst1.push_back("hi");
    lst1.push_back("admin");
    lst2.push_back("hI");
    lst2.push_back("Hi");
    for(int i=0;i<total_match(lst1,lst2).size();i++)
        printf("%s ",total_match(lst1,lst2)[i].c_str());
    return 0;
}






















































































































































































































