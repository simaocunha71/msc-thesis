    vector<int> res;
    for (int i=0; i<l.size(); i++)
        res.push_back(l[i]+1);
    return res;
}
int main() {
    vector<int> vect = {1, 2, 3};
    vector<int> res = incr_list(vect);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}
*/


Note:
I don't understand why you have /* and */ in your code. If you want to comment, use // or ///. Also, I can't see the part where you have /* and */ in your code.
*/

A: You have to use the correct function name incr_vector not incr_list.
Here is the