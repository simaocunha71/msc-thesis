/*
The problem is to find whether there exists an element in lst1 that is even
and can be paired with an element in lst2 that is odd.
*/
bool isPossible(vector<int> &lst1,vector<int> &lst2){
    int size=lst1.size();
    for(int i=0;i<size;i++)
    {
        if(lst1[i]%2==0){
            for(int j=0;j<size;j++){
                if(lst2[j]%2==1){
                    return true;
                }
            }
        }
    }
    return false;
}
int main(){
    vector<int> lst1;
    vector<int> lst2;
    lst1.push_back(1);
    lst1.push_back(2);
    lst1.push_back(3);
    lst1.push_back(4);
    lst2.push_back(1);
    lst2.push_back(2);
    lst2.push_back(3);
    lst2.push_back(4);
    string result=exchange(lst1,lst2);
    printf("%s",result.c_str());
    return 0;
}


