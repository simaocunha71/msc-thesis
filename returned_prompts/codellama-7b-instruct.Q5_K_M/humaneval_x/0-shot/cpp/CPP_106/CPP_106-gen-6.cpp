
/*

*/
vector<int> ans;
for(int i = 1; i <= n; i++){
    if(i % 2 == 0){
        ans.push_back(i);
    }else{
        int sum = 0;
        for(int j = 1; j <= i; j++){
            sum += j;
        }
        ans.push_back(sum);
    }
}
return ans;
}

int main(){
int n;
scanf("%d", &n);
vector<int> ans = f(n);
for(int i = 0; i < n; i++){
    printf("%d ", ans[i]);
}
return 0;
}
