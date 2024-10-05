    vector<int> result;
    sort(l1.begin(), l1.end());
    sort(l2.begin(), l2.end());

B:
    set_intersection(l1.begin(), l1.end(), l2.begin(), l2.end(),
                     back_inserter(result));

C:
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());

D:
    return result;
}


A: We first sort both vectors.

B: We find the common elements of the two vectors.

C: We sort and remove duplicates from the result.

D: Finally we return the result.
*/

