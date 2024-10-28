    vector<int> stones;
    for(int i=0; i<n; i++){
        if(n % 2 != 0){
            stones.push_back(n + (2 * i));
        }
        else{
            stones.push_back(n + (2 * i));
        }
    }
    return stones;
}

int main(){
    vector<int> res = make_a_pile(3);
    for(int i=0; i<res.size(); i++){
        printf("%d, ", res[i]);
    }
    return 0;
}
*/

