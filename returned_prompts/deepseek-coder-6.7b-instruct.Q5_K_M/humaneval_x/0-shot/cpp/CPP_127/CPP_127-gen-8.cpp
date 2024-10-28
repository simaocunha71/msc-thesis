  if(interval1[1] < interval2[0] || interval2[1] < interval1[0]) return "NO";

B:
  vector<int> intersect({max(interval1[0], interval2[0]), min(interval1[1], interval2[1])});

C:
  int len = intersect[1] - intersect[0];

D:
  if(len < 2) return "NO";

E:
  bool prime[len+1];
  for(int i=2;i<=len;i++) prime[i] = true;

F:
  for(int p=2;p*p<=len;p++){
    if(prime[p] == true){
      for(int i=p*p;i<=len;i += p)
        prime[i] = false;
    }
  }

G:
  return prime[len] ? "YES" : "NO";

}

int main(){
  printf("%s\n",intersection({1, 2}, {2, 3}).c_str());
  printf("%s\n",intersection({-1, 1}, {0, 4}).c_str());
  printf("%s\n",intersection({-3, -1}, {-5, 5}).c_str());
  return 0;
}

Note: This program is written in C++. It first checks whether the intervals intersect. If they do, it calculates the intersection interval and its length. Then it checks if the length is a prime number. If it is, it returns "YES", otherwise it returns "NO".

*/

#include<bits/stdc++.h>
using namespace std;

string isPrime(int n)
{
    if (n <= 1)
        return "NO";
    if (n <= 3)
        return "YES";
  
    if (n%2 == 0 || n%3 == 0)
        return "NO";
  
    for (int i=5; i*i<=n; i=i+6)
        if (n%i == 0 || n%(i+