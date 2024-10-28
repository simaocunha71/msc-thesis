/*
This is an algorithm problem, and I will use two pointers to solve it.
One pointer is used to record the position of the first odd number in lst1,
another pointer is used to record the position of the first odd number in lst2.
If there is an odd number in lst1, we will start to swap the elements between
lst1 and lst2.
*/


}
int main(){
    vector<int> lst1;
    vector<int> lst2;
    //Put your test cases here
    lst1 = {1, 2, 3, 4};
    lst2 = {1, 2, 3, 4};
    printf("%s\n", exchange(lst1, lst2).c_str());
    return 0;
}
