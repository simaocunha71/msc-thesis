    for (int i=0; i<l.size(); i++)
        for (int j=i+1; j<l.size(); j++)
            for (int k=j+1; k<l.size(); k++)
                if (l[i]+l[j]+l[k]==0)
                    return true;
    return false;
}

int main(){
    vector<int> l1 = {1, 3, 5, 0};
    vector<int> l2 = {1, 3, -2, 1};
    vector<int> l3 = {1, 2, 3, 7};
    vector<int> l4 = {2, 4, -5, 3, 9, 7};
    vector<int> l5 = {1};
    if (triples_sum_to_zero(l1)) printf("true\n");
    else printf("false\n");
    if (triples_sum_to_zero(l2)) printf("true\n");
    else printf("false\n");
    if (triples_sum_to_zero(l3)) printf("true\n");
    else printf("false\n");
    if (triples_sum_to_zero(l4)) printf("true\n");
    else printf("false\n");
    if (triples_sum_to_zero(l5)) printf("true\n");
    else printf("false\n");
    return 0;
}
