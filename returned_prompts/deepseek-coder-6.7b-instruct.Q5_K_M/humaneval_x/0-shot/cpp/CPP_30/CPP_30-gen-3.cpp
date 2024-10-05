    vector<int> positive;
    for(int i = 0; i < l.size(); i++){
        if(l[i] > 0){
            positive.push_back(l[i]);
        }
    }
    return positive;
}

int main(){
    vector<int> l = {-1, 2, -4, 5, 6};
    vector<int> positive = get_positive(l);
    for(int i = 0; i < positive.size(); i++){
        printf("%d ", positive[i]);
    }
    return 0;
}

*/

