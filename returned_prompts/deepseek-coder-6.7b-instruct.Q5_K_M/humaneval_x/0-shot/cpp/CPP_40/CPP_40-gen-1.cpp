  for(int i=0; i<l.size(); i++){
    for(int j=i+1; j<l.size(); j++){
      for(int k=j+1; k<l.size(); k++){
        if(l[i]+l[j]+l[k] == 0){
          return true;
        }
      }
    }
  }
  return false;
}

int main(){
  vector<int> vec1 = {1, 3, -2, 1};
  vector<int> vec2 = {2, 4, -5, 3, 9, 7};
  vector<int> vec3 = {1};
  printf("%d\n", triples_sum_to_zero(vec1));
  printf("%d\n", triples_sum_to_zero(vec2));
  printf("%d\n", triples_sum_to_zero(vec3));
  return 0;
}

Output:
1
1
0

Explanation:
The function triples_sum_to_zero takes a vector of integers as an argument. It uses three nested for-loops to iterate over all unique triplets of elements in the vector. If it finds a triplet where the sum of the elements is 0, it immediately returns true. If no such triplet is found after checking all triplets, it returns false.

The main function tests the triples_sum_to_zero function on three different vectors. The expected output is printed on the console.
*/


// The time complexity of this function is O(n^3) because it uses three nested loops to iterate over the vector.
// The space complexity is O(1) because it uses a constant amount of space to store the indices and the sum of the elements.

// Here, n is the size of the vector.

// This function could be optimized by sorting the vector and then using two pointers to find the triplets that sum to 0. The time complexity of this optimized version would be O(n^2).

// This function could be further optimized by using a hash set to store the elements of the vector. The time complexity of this optimized