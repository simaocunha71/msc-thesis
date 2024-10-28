    // a, b and c are the sides of the triangle
    // sort the sides in ascending order
    if(a > b){
        if(a > c){
            if(pow(c, 2) + pow(b, 2) == pow(a, 2))
                return true;
        }
        else{
            if(pow(a, 2) == pow(c, 2) + pow(b, 2))
                return true;
        }
    }
    else{
        if(b > c){
            if(pow(a, 2) + pow(c, 2) == pow(b, 2))
                return true;
        }
        else{
            if(pow(a, 2) + pow(b, 2) == pow(c, 2))
                return true;
        }
    }
    return false;
}
*/

