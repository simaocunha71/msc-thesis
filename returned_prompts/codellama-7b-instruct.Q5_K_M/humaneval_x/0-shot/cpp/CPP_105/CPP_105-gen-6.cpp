}
int main(){
   vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
   vector<string> ans = by_length(arr);
   for(int i=0; i<ans.size(); i++){
      cout << ans[i] << endl;
   }
}
