    int i=0,j=0,k=0,n=lst1.size(),m=lst2.size();
    while(i<n){
        if(lst1[i]%2==1){
            if(j>=m) return "NO";
            if(lst2[j]%2==1) {
                int tmp=lst2[j];
                lst2[j]=lst1[i];
                lst1[i]=tmp;
                i--;
                j++;
                continue A;
            }
            else {
                int tmp=lst2[j];
                lst2[j]=lst1[i];
                lst1[i]=tmp;
                j++;
                continue A;
            }
        }
        i++;
    }
    return "YES";
}

int main(){
    vector<int> lst1={1,2,3,4},lst2={1,2,3,4};
    printf("%s\n",exchange(lst1,lst2).c_str());
    lst1={1,2,3,4};lst2={1,5,3,4};
    printf("%s\n",exchange(lst1,lst2).c_str());
    return 0;
}

*/


































































































































































































