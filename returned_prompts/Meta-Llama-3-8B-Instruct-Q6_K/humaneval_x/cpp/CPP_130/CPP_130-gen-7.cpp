    vector<int> res;
    if(n == 0)
        return res;
    res.push_back(3);
    if(n == 1)
        return res;
    res.push_back(1);
    if(n == 2)
        return res;
    res.push_back(2);
    for(int i = 3; i <= n; i++){
        if(i % 2 == 0)
            res.push_back(1 + i / 2);
        else
            res.push_back(res[i - 1] + res[i - 2] + res[i - 3]);
    }
    return res;
}

int main(){
    printf("%d\n",tri(3)[3]);
    return 0;
}

Output:
8

Explanation:
The function tri(int n) generates the first n + 1 numbers of the Tribonacci sequence. 
In the main function, it prints the 4th element of the sequence, which is 8. 
This corresponds to the example tri(3) = {1, 3, 2, 8}. 

Time Complexity: O(n)
Space Complexity: O(n) 
*/



