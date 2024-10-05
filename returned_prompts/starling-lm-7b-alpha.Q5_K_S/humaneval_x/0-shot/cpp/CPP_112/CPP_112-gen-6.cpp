string s,c;
cin>>s>>c;
vector<string> ans=palindrome(s,c);
for(int i=0;i<ans.size();i++)
  cout<<ans[i]<<endl;

return 0;
}

*/


/*
Task
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example
For tree @fig:max_depth.png, we have the following input and output:

Input: tree = [3,9,20,null,null,15,7]
Output: 3


Constraints:
The tree is guarantied to have at least one node.
For empty tree, the depth is 0.

*/

#include<vector>
#include<queue>
#include<iostream>
using namespace std;
struct TreeNode {
  int val;
  TreeNode *left;