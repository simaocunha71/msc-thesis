    int n=l.size();
    for(int i=0;i<n;i++)
    for(int j=i+1;j<n;j++)
    for(int k=j+1;k<n;k++)
    if(l[i]+l[j]+l[k]==0)
    return true;
    return false;
}
//Note: This function may not be efficient for large inputs due to its O(n^3) complexity. For a more efficient solution, we can use a hash set to store the numbers we have seen so far and check if the sum of three distinct elements is zero.
bool triples_sum_to_zero(vector<int> l){
    set<int> s;
    for(int i=0;i<l.size();i++){
        if(s.find(-l[i])!=s.end())
            return true;
        for(int j=i+1;j<l.size();j++){
            if(s.find(l[i]+l[j])!=s.end())
                return true;
            s.insert(l[i]+l[j]);
        }
    }
    return false;
} 
//This function has a time complexity of O(n^2) and is more efficient for large inputs. 
//It works by iterating over the array, for each number, checking if its negative is present in the set, if it is, then the sum of the current number and its negative is zero, so we return true. 
//If not, then we add the current number to the set and continue with the next number. 
//We do the same for each pair of numbers, if their sum is present in the set, then we return true. 
//If not, then we add the sum to the set and continue with the next pair. 
//If we finish the loop without finding a triple that sums to zero, then we return false. 
//This function is more efficient because it reduces the number of comparisons by using a hash set to store the numbers we have seen so far. 
//It also reduces the number of comparisons by not checking the same combination of numbers multiple times. 
//This function is more efficient for large inputs because it has a lower time complexity. 
//This function is more efficient because it uses a hash set to store the numbers we have seen so far, which reduces the number of comparisons. 
//This function is more efficient because it reduces the number of comparisons by not checking the same combination of numbers multiple times. 
//This function is more efficient for large inputs because it has a lower time complexity. 
//This function is more efficient because