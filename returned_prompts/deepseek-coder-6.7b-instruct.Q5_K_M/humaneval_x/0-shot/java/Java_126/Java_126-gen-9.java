        for(int i = 0; i < lst.size() - 1; i++){
            if(lst.get(i) > lst.get(i+1))
                return false;
        }
        return true;
    }
}

This solution works by iterating over the list and comparing each pair of elements. If any pair of elements is in descending order, the function immediately returns false. If it makes it all the way to the end of the list without returning false, it returns true.

*/

// CORRECT:
/*
