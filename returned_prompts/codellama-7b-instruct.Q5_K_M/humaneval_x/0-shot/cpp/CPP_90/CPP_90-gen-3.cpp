    if(lst.size()<2) return NULL;
    sort(lst.begin(), lst.end());
    int i=0;
    for(i=0;i<lst.size();i++)
    {
        if(lst[i]!=lst[0]){
            return lst[i];
        }
    }
    return NULL;

}

int main(){
    vector<int> lst;
    int x;
    lst.push_back(1);
    lst.push_back(2);
    lst.push_back(3);
    lst.push_back(4);
    lst.push_back(5);
    printf("%d", next_smallest(lst));
}

