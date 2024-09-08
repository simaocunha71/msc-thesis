    int countEven=0;
    for(int i=0;i<lst1.size();i++){
        for(int j=0;j<lst2.size();j++){
            if(lst1[i]%2==0 && lst2[j]%2!=0){
                lst1[i]=lst2[j];
                lst2[j]=-1;
                countEven++;
            }
            else if(lst1[i]%2!=0 && lst2[j]%2==0){
                lst1[i]=-1;
                lst2[j]=lst1[i];
                countEven++;
            }
        }
    }
    if(countEven==lst1.size()){
        return "YES";
    }
    else{
        return "NO";
    }
}
int main(){
    vector<int> lst1={1, 2, 3, 4};
    vector<int> lst2={1, 2, 3, 4};
    printf("%s\n",exchange(lst1,lst2).c_str());
    return 0;
}

