    vector<string> lst_sum;
    sort(lst.begin(),lst.end());
    for(int i=0;i<lst.size();i++){
        if(lst[i].size()%2==1){
            lst.erase(lst.begin()+i);
            i--;
        }
    }
    return lst;
}
void test_case(){
    vector<string> lst={"aa", "a", "aaa"};
    printf("assert vector_sort({%s,%s,%s}) => {%s}\n",lst[0].c_str(),lst[1].c_str(),lst[2].c_str(),sorted_list_sum(lst)[0].c_str());
    vector<string> lst2={"ab", "a", "aaa", "cd"};
    printf("assert vector_sort({%s,%s,%s,%s}) => {%s,%s}\n",lst2[0].c_str(),lst2[1].c_str(),lst2[2].c_str(),lst2[3].c_str(),sorted_list_sum(lst2)[0].c_str(),sorted_list_sum(lst2)[1].c_str());
}
int main(){
    test_case();
    return 0;
}

*/


/*

In this question, we have to remove the strings with odd length from the vector and sort the vector by the length of the strings in ascending order.

To remove the strings with odd length from the vector, we can use the `erase` function of the `vector` class. This function takes an iterator to the element to be removed as the first parameter and returns an iterator to the next element after the removed element. We can pass the iterator of the element to be removed as `begin()+i` where `i` is the index of the element to be removed.

To sort the vector by the length of the strings in ascending order, we can use the `sort` function of the `vector` class. This function takes two iterators as parameters: the beginning and the end of the range to be sorted. We can pass the `begin()` and `end()