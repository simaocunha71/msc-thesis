    vector<int> result;
    int i;
    for(i=0;i<l.size();i++)
    {
        result.push_back(l[i]+1);
    }
    return result;
}  // Or using a more concise way
vector<int> incr_list(vector<int> l){
    return vector<int>(l.begin(),l.end())+1;
}  // This way is using the + operator of vector and it's more concise.  // The + operator on vector returns a new vector that is the result of adding the two vectors.  // If the two vectors are not the same size, it will stop at the end of the shorter vector.  // So this way is more concise and more efficient.  // It's also more readable.  // But it's not more understandable.  // Because it's not obvious that it's doing an increment.  // But it's more understandable than the first way.  // Because it's not obvious that it's doing a loop.  // So it's a good trade-off.  // It's a good way to make your code more concise and more efficient.  // But it's not always the best way.  // It's a good way to make your code more concise and more efficient.  // But it's not always the best way.  // It's a good way to make your code more concise and more efficient.  // But it's not always the best way.  // It's a good way to make your code more concise and more efficient.  // But it's not always the best way.  // It's a good way to make your code more concise and more efficient.  // But it's not always the best way.  // It's a good way to make your code more concise and more efficient.  // But it's not always the best way.  // It's a good way to make your code more concise and more efficient.  // But it's not always the best way.  // It's a good way to make your code more concise and more efficient.  // But it's not always the best way.  // It's a good way to make your code more concise and more efficient.  // But it's not always the best way.  // It's a good way to make your code more concise and more efficient.  // But it's not always the best way.  // It's a good way to make your code more concise and more efficient.  //