    int min_val = INT_MAX, min_idx = -1;
    for(int i = 0; i < arr.size(); i++){
        // check if the number is even and less than min_val
        if(arr[i] < min_val && arr[i] % 2 == 0){
            min_val = arr[i];
            min_idx = i;
        }
    }
    if(min_idx != -1) return {min_val, min_idx};
    else return {};
}
int main(){
    vector<int> arr = {4,2,3};
    vector<int> res = pluck(arr);
    for(int i=0; i<res.size(); i++)
    {
        printf("%d ", res[i]);
    }
    return 0;
}

*/

//src/code_challenges/tree/includes/tree.h
/*
 * tree.h
 *
 *  Created on: Aug 26, 2019
 *      Author: nishi
 */

#ifndef TREE_H_
#define TREE_H_

#include<iostream>
using namespace std;

struct Node {
	int data;
	Node* left;
	Node* right;

	Node(int data) {
		this->data = data;
		left = NULL;
		right = NULL;
	}
};

class Tree {
private:
	Node* root;
	void insert(int data, Node*& node);
	void inorder(Node* node);
	void preorder(Node* node);
	void postorder(Node* node);
public:
	Tree();
	void insert(int data);
	void inorder();
	void preorder();
	void postorder();
};

#endif /* TREE_H_ */

//src/code_challenges/tree/src/tree.cpp
/*
 * tree.cpp
 *
 *  Created on: Aug 26, 2019
 *      Author: nishi
 */

#include "tree.h"

Tree::Tree() {