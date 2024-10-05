    sort(lst.begin(), lst.end());
    vector<int> result;
    while(!lst.empty()){
        result.push_back(lst.front());
        lst.erase(lst.begin());
        if(!lst.empty()){
            result.push_back(lst.back());
            lst.pop_back();
        }
    }
    return result;
}

int main()
{
    vector<int> result = strange_sort_list({1, 2, 3, 4});
    for(int i=0; i<result.size(); i++)
        printf("%d ", result[i]);
    return 0;
}

The main function is there to test the function.

The function strange_sort_list is sorting the input vector in ascending order and then it uses a while loop to keep on popping the front and back elements from the vector and pushing them into the result vector.
This way it alternates between the smallest and largest elements of the vector.
*/

