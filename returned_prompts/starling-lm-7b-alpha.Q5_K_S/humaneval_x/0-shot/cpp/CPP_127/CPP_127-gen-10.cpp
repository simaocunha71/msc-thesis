    int x=0,y=0,z=0,n=0,m=0;
    x=interval1[1];
    y=interval1[0];
    z=interval2[1];
    n=interval2[0];
    m=z-n;
    if(x<n||y>z){
        return "NO";
    }
    for(int i=2;i<=m;i++){
        if(m%i==0){
            return "NO";
        }
    }
    return "YES";
}


int main()
{
    vector<int> a,b;
    char c;
    while(scanf("%d%c%d",&a[0],&c,&a[1])!=EOF){
        scanf("%d%c%d",&b[0],&c,&b[1]);
        printf("%s\n",intersection(a,b).c_str());
    }
    return 0;
}
















































*/

```
```

```
```

```
```

```
```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
