    if(lst1.size()>lst2.size()){
        return lst2;
    }else if(lst1.size()<lst2.size()){
        return lst1;
    }else{
        int sum1=0;
        for(int i=0;i<lst1.size();i++){
            sum1+=lst1[i].size();
        }
        int sum2=0;
        for(int i=0;i<lst2.size();i++){
            sum2+=lst2[i].size();
        }
        if(sum1<sum2){
            return lst1;
        }else if(sum2<sum1){
            return lst2;
        }else{
            for(int i=0;i<lst1.size();i++){
                if(lst1[i].size()>lst2[i].size()){
                    return lst2;
                }else if(lst1[i].size()<lst2[i].size()){
                    return lst1;
                }
            }
            return lst1;
        }
    }

}
int main(){
    vector<string> a={"1","2"};
    vector<string> b={"1","2","3","4"};
    printf("%s\n",total_match(a,b).empty()?"true":"false");
    return 0;
}

*/





































































































































































