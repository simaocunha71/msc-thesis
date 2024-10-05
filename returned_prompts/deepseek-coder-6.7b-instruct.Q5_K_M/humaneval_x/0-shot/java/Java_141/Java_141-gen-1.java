        int dot_position = file_name.indexOf('.');
        if (dot_position == -1 || dot_position == file_name.length() - 1){
            return "No";
        }
        String name = file_name.substring(0, dot_position);
        String extension = file_name.substring(dot_position + 1);

        if (!Character.isLetter(name.charAt(0))){
            return "No";
        }
        int digit_count = 0;
        for (char c : name.toCharArray()){
            if (Character.isDigit(c)){
                digit_count++;
            }
        }
        if (digit_count > 3){
            return "No";
        }

        if (!(extension.equals("txt") || extension.equals("exe") || extension.equals("dll"))){
            return "No";
        }
        return "Yes";
    }
}

This solution works by firstly checking if there is a dot in the string and if it is at the end of the string. If not, it returns "No". Then it splits the file name into the name part and the extension part. It checks if the first character of the name part is a letter. If not, it returns "No". It then counts the number of digits in the name part and if there are more than 3, it returns "No". Finally, it checks if the extension part is one of the allowed extensions and returns "Yes" or "No" accordingly.

*/

//T:
import org.junit.Test;
import static org.junit.Assert.*;

public class SolutionTest {
    @Test
    public void testFilenameCheck() {
        Solution sol = new Solution();
        assertEquals("Yes", sol.filenameCheck("example.txt"));
        assertEquals("No", sol.filenameCheck("1example.dll"));
        assertEquals("No", sol.filenameCheck("example.doc"));
        assertEquals("No", sol.filenameCheck("ex4mple.txt"));
        assertEquals("Yes", sol.filenameCheck("e1.txt"));
        assertEquals("No", sol.filenameCheck("1.txt"));
        assertEquals("No", sol