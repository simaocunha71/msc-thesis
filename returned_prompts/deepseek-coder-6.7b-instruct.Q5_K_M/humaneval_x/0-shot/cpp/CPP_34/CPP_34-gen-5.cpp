    sort(l.begin(), l.end());
    vector<int> unique_vector;
    unique_copy(l.begin(), l.end(), back_inserter(unique_vector));
    return unique_vector;
}


int main(){
    vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0,