    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());

B:
    vector<int> l3;
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(l3));
    return l3;
}


int main()
{
    vector<int> l1;
    vector<int> l2;
    vector<int> l3;
    l1 = {1, 4, 3, 34, 653, 2, 5};
    l2 = {5, 7, 1, 5, 9, 653, 121};
    l3 = common(l1,l2);
    for(int i=0;i<l3.size();i++){
        cout<<l3[i]<<" ";
    }
    return 0;
}
