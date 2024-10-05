    vector<int> result;
    for(int i=0;i<l1.size();i++){
        for(int j=0;j<l2.size();j++){
            if(l1[i]==l2[j]){
                result.push_back(l1[i]);
                break;
            }
        }
    }
    sort(result.begin(),result.end());
    result.erase(unique(result.begin(),result.end()),result.end());
    return result;
}

int main()
{
    vector<int> l1={5, 3, 2, 8};
    vector<int> l2={3, 2};
    vector<int> result = common(l1,l2);
    for(int i=0;i<result.size();i++){
        printf("%d ",result[i]);
    }
}


