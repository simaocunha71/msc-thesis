        Collections.sort(l);
        int middle = l.size()/2;
        if ( l.size() % 2 == 1 ) {
            return l.get(middle);
        } else {
            return (l.get(middle-1) + l.get(middle)) / 2.0;
        }
    }
}

This code sorts the list and then checks if the size of the list is odd or even. If it's odd, it returns the middle element, and if it's even, it calculates the average of the two middle elements.
The return type of the function is double because the average of two elements can be a decimal.
The function should work for lists of any length, including lists with an odd number of elements.

*/

