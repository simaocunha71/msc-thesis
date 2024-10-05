        if(dict.isEmpty())
            return false;
        boolean allUpper = true;
        boolean allLower = true;

B:
        for (Object key : dict.keySet()) {
            if (!(key instanceof String))
                return false;
            if(!((String)key).equals(((String)key).toLowerCase()))
                allUpper = false;
            if(!((String)key).equals(((String)key).toUpperCase()))
                allLower = false;
        }

C:
        return allUpper || allLower;
    }
}

Explanation:
The function starts by checking if the map is empty. If it is, it returns false.
Next, it initializes two boolean variables allUpper and allLower to true. These will keep track of whether all the keys in the map are upper case or lower case respectively.
Then it iterates over all the keys in the map. If a key is not a string, it returns false.
For each key, it checks if it is all upper case or all lower case by comparing the key to its lower case and upper case versions. If they are not equal, it sets the corresponding allUpper or allLower variable to false.
Finally, it returns the result of the logical OR of allUpper and allLower. This will be true if all the keys are either all upper case or all lower case. If not, it will be false.





























































































































































































