    int sum=0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]%2!=0 && i%2==0){
            sum+=lst[i];
        }
    }
    return sum;
}
int main(){
    vector<int> lst={30, 13, 24, 321};
    printf("%d\n", solutions(lst));
    return 0;
}

*/

#include<iostream>
#include<vector>
using namespace std;
int solution(vector<int> lst){

    int sum=0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]%2!=0 && i%2==0){
            sum+=lst[i];
        }
    }
    return sum;
}
int main(){
    vector<int> lst={30, 13, 24, 321};
    cout<<solution(lst)<<endl;
    return 0;
}




























































































































































































































































