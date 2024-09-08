```cpp
    sort(l.begin(),l.end());
    float mid;
    if(l.size()%2 == 0)
        mid = (l[l.size()/2-1]+l[l.size()/2])/2;
    else
        mid = l[l.size()/2];
    return mid;
}
```

B:
```cpp
    sort(l.begin(),l.end());
    float mid;
    if(l.size()%2 == 0)
        mid = (l[l.size()/2-1]+l[l.size()/2])/2.0;
    else
        mid = l[l.size()/2];
    return mid;
}
```

C:
```cpp
    sort(l.begin(),l.end());
    float mid;
    if(l.size()%2 == 0)
        mid = ((float)l[l.size()/2-1]+(float)l[l.size()/2])/2.0;
    else
        mid = l[l.size()/2];
    return mid;
}
```

D:
```cpp
    sort(l.begin(),l.end());
    float mid;
    if(l.size()%2 == 0)
        mid = ((float)l[l.size()/2-1]+(float)l[l.size()/2])/2.0;
    else
        mid = ((float)l[l.size()/2])/1.0;
    return mid;
}
```

E:
```cpp
    sort(l.begin(),l.end());
    float mid;
    if(l.size()%2 == 0)
        mid = ((float)l[l.size()/2-1]+(float)l[l.size()/2])/2.0;
    else
        mid = ((float)l[l.size()/2])/2.0;
    return mid;
}
```

F:
```cpp
    sort(l.begin(),l.end());
    float mid;
    if(l.size()%2 == 0)
        mid = ((float)l[l.size()/2-1]+(float)l[l.size()/2])/2.0;
    else
        mid = ((float)l[l.size()/2])/1.0;
    return (int)mid;
}
```
