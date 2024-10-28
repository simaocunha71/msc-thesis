        // write your solution here
        if(date.length() == 0) {
            return false;
        }

        String[] tokens = date.split("-");
        if(tokens.length != 3) {
            return false;
        }
        int month = Integer.parseInt(tokens[0]);
        int day = Integer.parseInt(tokens[1]);
        int year = Integer.parseInt(tokens[2]);

        if(month > 12 || month < 1) {
            return false;
        }
        if(month == 2) {
            if(day > 29 || day < 1) {
                return false;
            }
        } else if(month == 4 || month == 6 || month == 9 || month == 11) {
            if(day > 30 || day < 1) {
                return false;
            }
        } else {
            if(day > 31 || day < 1) {
                return false;
            }
        }

        return true;
    }
}


    /**
    You are given an array of integers. The length of the array is N and the range of the array is from -N to N. That means there are (2N + 1) different integers in the array. Now you have to find and return the sum of all the missing numbers in the array.
    Input Format
    The first line of input contains an integer, N, the length of the array. The second line contains N integers, separated by a single space.

    Constraints
    1 <= N <= 100000

    Output Format
    Print the sum of all the missing numbers.
    Sample Input
    STDIN              Standard Output
    ------------------------------------
    Input:
    3
    1 2 3
    Output:
    0
    Explanation
    Here, all the numbers from -3 to 3 are present in the array. So, the missing number's sum is 0.

    Input:
    STDIN              Standard Output
    ------------------------------------
    Input:
    3
    1 2 3
    Output:
    0
