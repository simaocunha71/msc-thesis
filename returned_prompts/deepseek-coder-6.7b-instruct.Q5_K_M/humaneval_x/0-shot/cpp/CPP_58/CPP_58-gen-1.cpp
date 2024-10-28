  sort(l1.begin(),l1.end());
  sort(l2.begin(),l2.end());

B:
  vector<int> result;
  set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),back_inserter(result));

C:
  sort(result.begin(),result.end());
  result.erase(unique(result.begin(), result.end()), result.end());

D:
  return result;
}

int main(){
  vector<int> l1,l2;
  l1 = {1, 4, 3, 34, 653, 2, 5};
  l2 = {5, 7, 1, 5, 9, 653, 121};
  vector<int> res = common(l1, l2);
  for(int i=0; i<res.size(); i++)
    printf("%d ",res[i]);
  return 0;
}


A: Sorting both vectors.
B: Finding the intersection of the vectors.
C: Sorting the result vector.
D: Returning the result vector.
*/

// Answer: 1, 5, 653

// Answer: 2, 3

/*

Explanation:

In the first example:
The sorted vectors are {1, 2, 3, 4, 5, 34, 653} and {1, 5, 5, 7, 9, 653, 121}.
The intersection of these two vectors is {1, 5, 653}. After sorting this vector, we get {1, 5, 653}.

In the second example:
The sorted vectors are {2, 3, 8} and {2, 3}.
The intersection of these two vectors is {2, 3}. After sorting this vector, we get {2, 3}.

*/

// Answer: 1, 5, 653

// Answer: 2, 