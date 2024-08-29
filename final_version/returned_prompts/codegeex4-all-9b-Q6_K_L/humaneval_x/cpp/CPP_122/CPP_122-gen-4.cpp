    int sum=0;
    for(int i=0;i<k;i++){
        if(arr[i]<100){
            sum+=arr[i];
        }
    }
    return sum;
}
int main(){
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    printf("%d\n",add_elements(arr,k)); //24
    return 0;
}
E:
    #include<stdio.h>
    #include<vector>
    using namespace std;
    int add_elements(vector<int> arr,int k){
        int sum=0;
        for(int i=0;i<k;i++){
            if(arr[i]<10){
                sum+=arr[i];
            }else if(arr[i]<100){
                sum+=arr[i];
            }
        }
        return sum;
    }
    int main(){
        vector<int> arr = {111,21,3,4000,5,6,7,8,9};
        int k = 4;
        printf("%d\n",add_elements(arr,k)); //24
        return 0;
    }
C:
    #include<stdio.h>
    #include<vector>
    using namespace std;
    int add_elements(vector<int> arr,int k){
        int sum=0;
        for(int i=0;i<k;i++){
            if(arr[i]<10){
                sum+=arr[i];
            }else if(arr[i]<100){
                sum+=arr[i];
            }else if(arr[i]<1000){
                sum+=arr[i];
            }
        }
        return sum;
    }
    int main(){
        vector<int> arr = {111,21,3,4000,5,6,7,8,9};
        int k = 4;
        printf("%d\n",add_elements(arr,k)); //24
        return 0;
    }
W:
    #include<stdio.h>
    #include<vector>
    using namespace std;
    int add_elements(vector<int> arr,int k){
        int sum=0;
        for(int i=0;i<k;i++){
            if(arr[i]<10){
                sum+=arr[i];
            }else if(arr[i]<100){
                sum+=arr[i];
            }else if(arr[i]<1000){
                sum+=arr[i];
            }else if(arr[i]<10000){
                sum+=arr[i];
            }
        }
        return sum;
    }
    int main(){
       