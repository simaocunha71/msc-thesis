
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
    if len(lst1) == 0 || len(lst2) == 0{ return nil}
    
    if len(lst1[0]) < len(lst2[0]{
        for i:= 0;i<len(lst1);++i{
            totalMatch := TotalMatch(lst1[0:], lst2)
            
            if totalMatch == nil || len(totalMatch) == 0 {
                return nil
            }else{
               lst2 = append(lst2, lst1...)
               break   // add the first element to the list of the result.
            }
        }
        
    }) else if len(lst1[0]) > len(lst2[0]{
        for i:= 0;i<len(lst2);++i{
            totalMatch := TotalMatch(lst2[0:], lst1)
            
            if totalMatch == nil || len(totalMatch) == 0 {
                return nil
            }else{
               lst1 = append(lst1, lst2...)
                break   // add the last element to the list of the result.
            }
        }
        
    }) else if len(lst1[0]) < len(lst2[0]{
        totalMatch := TotalMatch(