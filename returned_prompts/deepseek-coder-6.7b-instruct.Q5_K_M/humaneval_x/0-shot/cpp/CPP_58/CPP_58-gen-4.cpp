    vector<int> result;

    sort(l1.begin(), l1.end());
    sort(l2.begin(), l2.end());

    set_intersection(l1.begin(), l1.end(), l2.begin(), l2.end(), back_inserter(result));

    result.erase(unique(result.begin(), result.end()), result.end());

    return result;
}

int main(){
    vector<int> l1, l2;
    int a[] = {1, 4, 3, 34, 653, 2, 5};
    int b[] = {5, 7, 1, 5, 9, 653, 121};

    l1.assign(a, a+7);
    l2.assign(b, b+7);

    vector<int> result = common(l1, l2);

    for(int i=0; i<result.size(); i++