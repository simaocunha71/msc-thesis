    sort(l.begin(), l.end());
    l.erase(unique(l.begin(), l.end()), l.end());
    return l;
}

int main(){
    vector<int> l {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> u = unique(l);
    for(int i=0; i<u.size(); i++)
        printf("%d ", u[i]);
    return 0;
}

*/

