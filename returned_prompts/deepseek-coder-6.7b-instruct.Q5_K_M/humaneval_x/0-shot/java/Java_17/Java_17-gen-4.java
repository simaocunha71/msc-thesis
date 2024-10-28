        List<Integer> result = new ArrayList<Integer>();
        String[] notes = string.split(" ");
        for (String note : notes) {
            if (note.equals("o")) {
                result.add(4);
            } else if (note.equals("o|")) {
                result.add(2);
            } else if (note.equals(".|")) {
                result.add(1);
            }
        }
        return result;
    }
}

This code splits the input string into individual notes, then checks each one against the provided note types. Each note type gets added to the result list the correct number of times.
*/

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.parseMusic("o o| ."));
    }
}

//src/test/java/MusicParserTest.java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;

class SolutionTest {
    Solution sol = new Solution();

    @Test
    void parseMusicTest1() {
        assertEquals(Arrays.asList(4, 2, 1), sol.parseMusic("o o| ."));
    }

    @Test
    void parseMusicTest2() {
        assertEquals(Arrays.asList(4, 4, 2, 2, 1, 1, 1, 1, 4, 4), sol.parseMusic("o o| .| o| o| .| .| .| .| o o"));
    }

    @Test
    void parseMusicTest3() {
        assertEquals(Arrays.asList(4, 2, 1, 1, 4, 2, 1, 1, 4), sol.parseMusic("o o| .| .| o o| .| .| o"));
    }
}

/*
This JUnit test class tests the parseMusic method of the Solution class. It tests the function with various inputs and checks that the output is correct.
