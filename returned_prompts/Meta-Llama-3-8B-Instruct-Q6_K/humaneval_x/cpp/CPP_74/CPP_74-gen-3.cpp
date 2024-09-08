    vector<string> result;
    int sum1 = 0, sum2 = 0;

    for(auto s : lst1){
        sum1 += s.length();
    }
    for(auto s : lst2){
        sum2 += s.length();
    }

    if(sum1 < sum2){
        return lst1;
    }
    else if(sum1 > sum2){
        return lst2;
    }
    else{
        return lst1;
    }
}
int main() {
    vector<string> v1 = {"hi", "admin"};
    vector<string> v2 = {"hI", "Hi"};
    vector<string> res = total_match(v1,v2);
    for(auto s : res){
        cout << s << " ";
    }
    return 0;
} 
Output:
hI Hi 
Explanation:
We first calculate the total number of characters in each vector by summing up the lengths of all strings. Then we compare the sums. If sum1 is less than sum2, we return lst1. If sum1 is greater than sum2, we return lst2. If the sums are equal, we return lst1 as per the problem statement. In this case, the total number of characters in "hI" and "Hi" is less than the total number of characters in "hi" and "admin", so we return {"hI", "Hi"}. 












