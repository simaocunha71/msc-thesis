    vector<int> result;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    vector<int>::iterator i = set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(result));
    result.erase(i,result.end());
    return result;
}
int main()
{
    vector<int> v1 = {1,4,3,34,653,2,5};
    vector<int> v2 = {5,7,1,5,9,653,121};
    vector<int> res = common(v1,v2);
    for(int i=0; i<res.size(); i++)
        printf("%d ",res[i]);
    printf("\n");
    return 0;
}
B:
    vector<int> result;
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(result));
    sort(result.begin(),result.end());
    result.erase(unique(result.begin(),result.end()),result.end());
    return result;
}
C:
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(result));
    sort(result.begin(),result.end());
    result.erase(unique(result.begin(),result.end()),result.end());
    return result;
}
D:
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(result));
    result.unique();
    return result;
}
E:
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(result));
    sort(result.begin(),result.end());
    result.erase(unique(result.begin(),result.end()),result.end());
    return result;
}
F:
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(result));
    result.erase(unique(result.begin(),result.end()),result.end());
    return result;
}
G:
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(result));
    return result;
}
H:
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(result));
    result.unique();
    return result;
}

I:
    vector<int> result;
    set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(result));
    sort(result.begin(),result.end());
    return result;
