const lst = ["aa", "a", "aaa"]
const lst2 = ["ab", "a", "aaa", "cd"]

function list_sort(list) {
    let result = list.filter(item => item.length % 2 === 0);
    result.sort((a, b) => {
        if (a.length < b.length) {
            return -1;
        } else if (a.length > b.length) {
            return 1;
        } else {
            if (a < b) {
                return -1;
            } else {
                return 1;
            }
        }
    })
    return result;
}

console.log(list_sort(lst)) //=> ["aa"]
console.log(list_sort(lst2)) //=> ["ab", "cd"]

/*
The above code first filters out the strings that have odd lengths from the list.
Then, it sorts the list based on the length of the strings.
Finally, it returns a sorted list of strings in ascending order by length,
 and if two strings have the same length, they are sorted alphabetically.

The function uses the filter() method to remove the strings with odd lengths from the list.
It uses the sort() method to sort the strings based on their length.
The sort() method takes a compare function as an argument, which determines the order of the strings.
If a.length < b.length, -1 is returned, which means that a comes before b in the sorted list.
If a.length > b.length, 1 is returned, which means that a comes after b in the sorted list.
If a.length === b.length, the strings are sorted alphabetically.

The function returns a new list that contains only the strings with even lengths, sorted by length and alphabetically.
*/

*/

/*
The above code first filters out the strings that have odd lengths from the list.
Then, it sorts the list based on the length of the strings.
Finally, it returns a sorted list of strings in ascending order by length,
 and if two strings have the same length, they are sorted alphabetically.

The function uses the filter() method to remove