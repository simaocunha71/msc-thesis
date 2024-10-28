    vector<int> result(l.size());
    vector<int> temp;
    for(int i = 0; i<l.size();i++){
        if((i+1)%3==0)
            temp.push_back(l[i]);
    }
    sort(temp.begin(),temp.end());
    for(int i = 0,j=0; i<l.size();i++){
        if((i+1)%3==0)
            result[i]=temp[j++];
        else
            result[i]=l[i];
    }
    return result;
}
int main(){
    vector<int> l = {5, 6, 3, 4, 8, 9, 2};
    vector<int> result = sort_third(l);
    for(int i = 0; i<result.size();i++)
        printf("%d ",result[i]);
    return 0;
}
*/

