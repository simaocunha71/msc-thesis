    int size1 = lst1.size();
    int size2 = lst2.size();
    int flag = 0;
    for(int i = 0;i < size1;i++){
        if(lst1[i] % 2 != 0){
            flag = 1;
            break;
        }
    }
    if(flag == 0){
        return "YES";
    }
    for(int i = 0;i < size1;i++){
        if(lst1[i] % 2 == 0){
            int temp = lst1[i];
            lst1[i] = lst2[i];
            lst2[i] = temp;
        }
    }
    for(int i = 0;i < size1;i++){
        if(lst1[i] % 2 != 0){
            return "NO";
        }
    }
    return "YES";
}
int main(){
    vector<int> a = {1, 2, 3, 4};
    vector<int> b = {1, 2, 3, 4};
    printf("The result is %s\n",exchange(a,b).c_str());
    return 0;
}

*/











































































































































































































