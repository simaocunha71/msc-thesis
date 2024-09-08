    vector<int> common_elements;

    // Create a set of elements from the first list
    set<int> s1(l1.begin(), l1.end());

    // Create a set of elements from the second list
    set<int> s2(l2.begin(), l2.end());

    // Find the intersection of the two sets
    set<int> intersection;
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                     inserter(intersection, intersection.begin()));

    // Convert the intersection set to a vector and sort it
    vector<int> result(intersection.begin(), intersection.end());
    sort(result.begin(), result.end());

    // Return the vector of unique common elements
    return result;

}

int main()
{
    vector<int> v1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> v2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> common_elements = common(v1,v2);
    for(int i = 0 ; i < common_elements.size() ; i++)
    {
        printf("%d ",common_elements[i]);
    }
    printf("\n");
    return 0;
}

B:
    vector<int> common(vector<int> l1,vector<int> l2){
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());
    vector<int> common_elements;
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),back_inserter(common_elements));
    sort(common_elements.begin(), common_elements.end());
    return common_elements;
}
int main()
{
    vector<int> v1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> v2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> common_elements = common(v1,v2);
    for(int i = 0 ; i < common_elements.size() ; i++)
    {
        printf("%d ",common_elements[i]);
    }
    printf("\n");
    return 0;
}C:
    vector<int> common(vector<int> l1,vector<int> l2){
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l