        //split string by spaces and store in an array
        String[] splitArray = s.split(" ");

        //get number of apples and oranges
        int apples = Integer.parseInt(splitArray[0]);
        int oranges = Integer.parseInt(splitArray[2]);

        //calculate the number of mangoes
        int mangoes = n - apples - oranges;

        return mangoes;
    }
}

This solution assumes that the input string will always follow the format specified in the problem statement. It splits the string by spaces, converts the two numbers to integers, and then subtracts the sum of the apples and oranges from the total number of fruits to find the number of mangoes.
*/

// 