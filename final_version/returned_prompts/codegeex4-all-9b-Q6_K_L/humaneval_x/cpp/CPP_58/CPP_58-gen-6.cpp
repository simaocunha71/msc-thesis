vector<int> ret;
    //vector<int> ret;
    //for(int i=0;i<l1.size();i++)
    //    for(int j=0;j<l2.size();j++)
    //        if(l1[i]==l2[j])
    //            ret.push_back(l1[i]);
    //sort(ret.begin(),ret.end());
    //ret.erase(unique(ret.begin(),ret.end()),ret.end());
    //return ret;

B:
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    int i=0,j=0;
    while(i<l1.size()&&j<l2.size()){
        if(l1[i]<l2[j]){
            i++;
            continue;
        }
        else if(l1[i]>l2[j]){
            j++;
            continue;
        }
        else{
            ret.push_back(l1[i]);
            i++;
            j++;
        }
    }
    sort(ret.begin(),ret.end());
    ret.erase(unique(ret.begin(),ret.end()),ret.end());
    return ret;
}
int main(){
    vector<int> l1={1, 4, 3, 34, 653, 2, 5};
    vector<int> l2={5, 7, 1, 5, 9, 653, 121};
    vector<int> l3={5, 3, 2, 8};
    vector<int> l4={3, 2};
    vector<int> ret;
    ret=common(l1,l2);
    for(int i=0;i<ret.size();i++)
        printf("%d ",ret[i]);
    printf("\n");
    ret=common(l3,l4);
    for(int i=0;i<ret.size();i++)
        printf("%d ",ret[i]);
    printf("\n");
    return 0;
}

