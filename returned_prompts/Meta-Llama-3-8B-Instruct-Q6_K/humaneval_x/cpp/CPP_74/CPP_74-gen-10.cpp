    int total1=0,total2=0;
    for(auto &s:lst1){
        total1+=s.size();
    }
    for(auto &s:lst2){
        total2+=s.size();
    }
    if(total1<total2){
        return lst1;
    }
    else if(total1>total2){
        return lst2;
    }
    else{
        return lst1;
    }
}
int main()
{
    vector<string> lst1={"hi", "admin"};
    vector<string> lst2={"hI", "Hi"};
    vector<string> result = total_match(lst1, lst2);
    for(auto &s:result){
        printf("%s\n",s.c_str());
    }
    return 0;
}

Output:
hI
Hi

Explanation:
The function total_match is used to compare the total number of characters in two lists of strings. It iterates over each string in the lists, sums up the length of each string, and then compares the total sums. If the total sum of the first list is less than the second, it returns the first list. If the total sum of the first list is greater than the second, it returns the second list. If the sums are equal, it returns the first list. In the given example, the total number of characters in the first list is 7 (hi + admin = 7), and the total number of characters in the second list is 5 (hI + Hi = 5). Therefore, the function returns the second list. 