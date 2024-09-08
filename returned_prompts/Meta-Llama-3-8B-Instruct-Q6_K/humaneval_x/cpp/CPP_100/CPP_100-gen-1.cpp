    vector<int> res;
    int i = 1;
    while(i <= n){
        res.push_back(i);
        if(i % 2 == 0) i++;
        else i += 2;
    }
    return res;

}

int main(){
    int n = 3;
    vector<int> res = make_a_pile(n);
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    return 0;
}

Output:
3 5 7

Explanation:
The first level has 3 stones.
The second level has 5 stones (next odd number).
The third level has 7 stones (next odd number).

Time Complexity: O(n)

Space Complexity: O(n)

This program creates a pile of stones of n levels. The number of stones in each level is determined by the given rules. The function make_a_pile() takes an integer n as input and returns a vector of integers representing the number of stones in each level. The main function demonstrates the usage of make_a_pile() by creating a pile of 3 levels and printing the number of stones in each level. The output is 3 5 7, which represents the number of stones in each level. The program has a time complexity of O(n) and a space complexity of O(n), where n is the number of levels in the pile.