        String binary = Integer.toBinaryString(decimal);
        String result = "db" + binary + "db";
        return result;
    }
}

The Integer.toBinaryString(int) function in Java converts a decimal number to binary format. It takes an integer as an argument and returns a string that contains the binary representation of that number.
*/

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.decimalToBinary(15)); // returns "db1111db"
        System.out.println(sol.decimalToBinary(32)); // returns "db100000db"
    }
}

/*
Output:
db1111db
db100000db
*/

// Java program to convert decimal to binary with extra characters 'db'

/*
Explanation:

The given problem is to convert a decimal number to its binary equivalent. We are asked to return the binary as a string, with each character representing a binary digit. Each character in the string will be ‘0’ or ‘1’. We will add 'db' at the beginning and end of the string to help with the format.

We use the Integer.toBinaryString(int) method in Java, which converts a decimal number to a binary string. It takes an integer as an argument and returns a string that contains the binary representation of that number.

Finally, we concatenate 'db' to both sides of the binary string and return the result.

In the main method, we test our solution with the examples provided in the problem statement.
*/

// Time complexity: O(log(N))
// Space complexity: O(log(N))

// Where N is the decimal number.

// This code was written by Gautam Kunwar.
// I am sharing it under GNU General Public License v3.0.
// You should have received a copy of the GNU General Public License along with this program.
// If not, see <https://www.gnu.org/licenses/>.
// Please contact the author if you have any questions.
// Author's Github link: https://github