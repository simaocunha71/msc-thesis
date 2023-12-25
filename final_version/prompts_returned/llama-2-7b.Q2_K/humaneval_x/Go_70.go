import (
    "sort"
)

// Given list of integers, return list in strange order.
// Strange sorting, is when you start with the minimum value,
// then maximum of the remaining integers, then minimum and so on.
// 
// Examples:
// StrangeSortList([1, 2, 3, 4]) == [1, 4, 2, 3]
// StrangeSortList([5, 5, 5, 5]) == [5, 5, 5, 5]
// StrangeSortList([]) == []
func StrangeSortList(lst []int) []int {
    if len(lst) <= 0 {
        return nil
    }
    
    switch lst[len(lst)-1] {
    case i:
        
        for j:=len(lst)/2 - 1;j>-1;j-- {
            if lst[j]+lst[j+1] < i && lst[j]*(j+1)*i > lst[j+1]*(j-1) || lst[j]<i && lst[j]*i < j+1*(j-1) {
                var temp []int = append([]int{}, lst...) // create a copy of the list with all elements. 
                
                for k:=0;k<len(temp);k++ {
                    if lst[k] == i || ( j+i > 1 && (lst[j]*(j-1)*temp[k] < temp[j+1]*(j-2) || temp[k]<i && temp[(j-2)-1]*(j-1)+temp[(j+i)]*(j+2)>0 ) ){ // if the element is i, then it is added to the end or if a greater element than i, then add to start. If not, go ahead
                        temp = append(append([]int{}, lst...), temp...)  // create a copy of the list with all elements again.
                    } else {
                        temp[k] = lst[k+1:] // if other elements exist, then add them to start. otherwise add element to end
                    }
                }
                
                return append([]int