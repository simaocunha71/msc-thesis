  sort(l.begin(), l.end());
  int sum;
  for(int i=0; i<l.size()-2; i++){
    int j = i + 1;
    int k = l.size() - 1;
    while(j < k){
      sum = l[i] + l[j] + l[k];
      if(sum < 0){
        j += 1;
      }
      else if(sum > 0){
        k -= 1;
      }
      else{
        return true;
      }
    }
  }
  return false;
}

int main() {
    vector<int> v1 = {1, 3, 5, 0};
    vector<int> v2 = {1, 3, -2, 1};
    vector<int> v3 = {1, 2, 3, 7};
    vector<int> v4 = {2, 4, -5, 3, 9, 7};
    vector<int> v5 = {1};

    printf("%d\n", triples_sum_to_zero(v1)); // 0 (False)
    printf("%d\n", triples_sum_to_zero(v2)); // 1 (True)
    printf("%d\n", triples_sum_to_zero(v3)); // 0 (False)
    printf("%d\n", triples_sum_to_zero(v4)); // 1 (True)
    printf("%d\n", triples_sum_to_zero(v5)); // 0 (False)

    return 0;
}

Time complexity: O(n^2)
Space complexity: O(1)

This solution works by sorting the input vector first. Then, it uses two pointers method to find three numbers in the vector that sum to zero. The two pointers method starts from the beginning and end of the vector, and moves inwards if the sum of the three numbers is less than zero or more than zero. If the sum is equal to zero, it returns true. If it cannot find three numbers that sum to zero, it returns false.
*/
