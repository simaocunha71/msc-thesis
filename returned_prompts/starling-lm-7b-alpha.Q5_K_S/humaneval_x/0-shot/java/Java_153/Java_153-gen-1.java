    int max = 0;
    String res = "";
    for(int i = 0;i<extensions.size();i++){
        int tmp = 0;
        int cnt = 0;
        for(int j = 0;j<extensions.get(i).length();j++){
            if(extensions.get(i).charAt(j)>=65 && extensions.get(i).charAt(j)<=90)
                cnt++;
            else
                tmp--;
        }
        if(tmp>max){
            max = tmp;
            res = extensions.get(i);
        }
    }
    return class_name + "." + res;
    }
}




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

``