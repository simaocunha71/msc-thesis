        // Your code here
        return null;
    }
}

*/

import java.util.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        if (arr.isEmpty()) return new ArrayList<>();
        int min = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < min && arr.get(i) % 2 == 0) {
                min = arr.get(i);
                minIndex = i;
            }
        }
        if (minIndex == -1) return new ArrayList<>();
        return Arrays.asList(min, minIndex);
    }
}

//src/main/java/com/coderpad/tree/TreeNode.java
package com.coderpad.tree;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;

    public TreeNode(int x) {
        val = x;
    }
}

//src/main/java/com/coderpad/tree/TreeProblems.java
package com.coderpad.tree;

import java.util.*;

public class TreeProblems {
    /*
    Given a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its level order traversal as:
    [
      [3],
      [9,20],
      [15,7]
    ]
    */
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if(root == null) return result;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while