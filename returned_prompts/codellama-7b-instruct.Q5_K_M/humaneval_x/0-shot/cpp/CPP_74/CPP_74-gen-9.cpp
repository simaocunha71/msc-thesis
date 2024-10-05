    int i,j;
    int count1=0;
    int count2=0;

    for(i=0;i<lst1.size();i++){
        for(j=0;j<lst1[i].size();j++){
            count1+=lst1[i][j];
        }
    }
    for(i=0;i<lst2.size();i++){
        for(j=0;j<lst2[i].size();j++){
            count2+=lst2[i][j];
        }
    }
    if(count1>count2){
        return lst1;
    }
    else{
        return lst2;
    }
}
int main(){
    vector<string>lst1 = {"hi", "admin"};
    vector<string>lst2 = {"hI", "Hi"};
    vector<string>res= total_match(lst1,lst2);
    for(int i=0;i<res.size();i++){
        printf("%s ",res[