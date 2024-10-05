    vector<int> m;
    for(int i = 0; i < l.size(); i++){
        if((i+1)%3 == 0) m.push_back(l[i]);
    }
    sort(m.begin(), m.end());
    for(int i = 0, j = 0; i < l.size(); i++){
        if((i+1)%3 == 0) l[i] = m[j++];
    }
    return l;
}

int main(){
    vector<int> v = {5, 6, 3, 4, 8, 9, 2};
    v = sort_third(v);
    for(int i = 0; i < v.size(); i++){
        printf("%d ", v[i]);
    }
    printf("\n");
    return 0;
}
*/

