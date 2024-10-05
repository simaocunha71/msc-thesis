    vector<int> sorted;
    for(int i=0; i<l.size(); i++){
        if((i+1)%3 == 0) sorted.push_back(l[i]);
    }
    sort(sorted.begin(), sorted.end());
    for(int i=0, j=0; i<l.size(); i++){
        if((i+1)%3 == 0) l[i] = sorted[j++];
    }
    return l;
}

int main(){
    vector<int> v = {5, 6, 3, 4, 8, 9, 2};
    v = sort_third(v);
    for(int i=0; i<v.size(); i++) printf("%d ", v[i]);
    return 0;
}
```


## Translation Key: thursday_afternoon
```
thursday_afternoon
```
translations:

```json
"thursday_afternoon": "Jueves por la tarde"
```


## Translation Key: thursday_afternoon_x
```
thursday_afternoon_x
```
translations:

```json
"thursday_afternoon_x": "Jueves por la tarde: %s"
```


## Translation Key: tuesday_afternoon
```
tuesday_afternoon
```
translations:

```json
"