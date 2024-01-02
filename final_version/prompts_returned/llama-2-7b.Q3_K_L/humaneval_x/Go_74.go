
// Write a function that accepts two lists of strings and returns the list that has
// total number of chars in the all strings of the list less than the other list.
// 
// if the two lists have the same number of chars, return the first list.
// 
// Examples
// TotalMatch([], []) ➞ []
// TotalMatch(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
// TotalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
// TotalMatch(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
// TotalMatch(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
func TotalMatch(lst1 []string,lst2 []string) []string {
    if len(lst1) == len(lst2){
        return lst1;
    }
    sum1 := 0
    sum2 := 0
    for i:= range lst1{
        if lst1[i] != "" && lst1[i] != " " {
            sum1++
        }
    }
    for i:=range lst2{
        if lst2[i] != "" && lst2[i] != " " {
            sum2++
        }
    }
    if (sum1+sum2) >= len(lst1){
        return lst2;
    	return lst1;
    } else{
        return lst1;
    } 
}