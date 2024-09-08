    vector<int> res;
    set<int> s1(l1.begin(),l1.end());
    set<int> s2(l2.begin(),l2.end());
    set<int> inter;
    set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),std::inserter(inter,inter.begin()));
    for(int i:inter){
        res.push_back(i);
    }
    sort(res.begin(),res.end());
    return res;

B:
    vector<int> res;
    set<int> s1(l1.begin(),l1.end());
    set<int> s2(l2.begin(),l2.end());
    set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),std::inserter(res,res.begin()));
    return res;

C:
    vector<int> res;
    set<int> s1(l1.begin(),l1.end());
    set<int> s2(l2.begin(),l2.end());
    set<int> inter;
    set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),std::inserter(inter,inter.begin()));
    for(int i:inter){
        res.push_back(i);
    }
    sort(res.begin(),res.end());
    res.erase(unique(res.begin(),res.end()),res.end());
    return res;

D:
    vector<int> res;
    set<int> s1(l1.begin(),l1.end());
    set<int> s2(l2.begin(),l2.end());
    set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),std::inserter(res,res.begin()));
    sort(res.begin(),res.end());
    res.erase(std::unique(res.begin(),res.end()),res.end());
    return res;

}
int main(){
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> res = common(l1,l2);
    for(int i:res){
        printf("%d ",i);
    }
    printf("\n");
    return 0;
}

Answer: C

Explanation:
The problem is asking to find the common elements in two vectors and return them in sorted and unique form. 

The correct solution is C, which first finds the common elements using the set_intersection function, then sorts the result and