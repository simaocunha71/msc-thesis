
// Write a function that returns the size of a given tree.
// If the tree is not a binary search tree, return -1.
// Example:
// Tree(1, 2, 3, 4, 5) => 5
// Tree(1, 2, 3, 4, 5, 6) => -1
type TreeNode struct {
  Value int
  Left *TreeNode
  Right *TreeNode
}

func Tree(values ...int) *TreeNode {
  root := &TreeNode{}

  var current *TreeNode
  for _, v := range values {
    if v == 0 {
      continue
    }
    if v < 0 {
      return nil
    }
    node := &TreeNode{Value: v}
    if current == nil {
      current = node
    } else {
      if v < current.Value {
        if current.Left == nil {
          current.Left = node
        } else {
          current = current.Left
          for current.Right != nil {
            current = current.Right
          }
          current.Right = node
        }
      } else {
        if current.Right == nil {
          current.Right = node
        } else {
          current = current.Right
          for current.Left != nil {
            current = current.Left
          }
          current.Left = node
        }
      }
    }
  }

  return root
}

func TreeSize(root *TreeNode) int {
  if root == nil {
    return 0
  }

  l := TreeSize(root.Left)
  if l < 0 {
    return -1
  }
  r := TreeSize(root.Right)
  if r < 0 {
    return -1
  }

  return l + r + 1
}

func main() {
  fmt.Println(TreeSize(Tree(1, 2, 3, 4, 5)))
  fmt.Println(TreeSize(Tree(1, 2, 3, 4, 5, 6)))
}
