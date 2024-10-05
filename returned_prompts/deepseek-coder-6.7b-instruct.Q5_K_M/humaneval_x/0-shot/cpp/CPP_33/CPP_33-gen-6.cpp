    int n = l.size();
    vector<int> indexes;
    for(int i=0; i<n; i++){
        if((i+1)%3 == 0){
            indexes.push_back(l[i]);
        }
    }
    sort(indexes.begin(), indexes.end());
    for(int i=0; i<n; i++){
        if((i+1)%3 == 0){
            l[i] = indexes[i/3];
        }
    }
    return l;
}
int main(){
    vector<int> l = {5, 6, 3, 4, 8, 9, 2};
    vector<int> l_prime = sort_third(l);
    for(int i=0; i<l_prime.size(); i++){
        printf("%d ", l_prime[i]);
    }
    return 0;
}
*/

