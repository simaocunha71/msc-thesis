    int num = (int)Math.ceil(Double.parseDouble(value));
    return num;
}

    public int countLower(String value)  {

B:
    int num = (int)Math.floor(Double.parseDouble(value));
    return num;
}

public int closestInteger(String value) {

C:
    int up = countUpper(value);
    int low = countLower(value);
    if (Math.abs(up - Integer.parseInt(value)) < Math.abs(low - Integer.parseInt(value)))
        return up;
    else if(Math.abs(up - Integer.parseInt(value)) > Math.abs(low - Integer.parseInt(value)))
        return low;
    else 
        return up;
}

public static void main(String[] args) {
    Solution s = new Solution();
    System.out.println(s.closestInteger("10")); //10
    System.out.println(s.closestInteger("15.3")); //15
    System.out.println(s.closestInteger("14.5")); //15
    System.out.println(s.closestInteger("-14.5")); //-15
}
}

The function closestInteger takes a string value representing a number. It first calculates the upper and lower bounds of the number by using the Math.ceil and Math.floor functions respectively. It then compares the absolute difference between these bounds and the original number. The function returns the bound with the smallest absolute difference. If both are equal, it returns the upper bound.

The function countUpper and countLower are helper functions that calculate the upper and lower bounds of the number respectively.

The main method tests the function with several examples.

The time complexity of the function is O(1), as it performs a constant number of operations. The space complexity is also O(1), as it uses a constant amount of space to store the upper and lower bounds and the original number.
