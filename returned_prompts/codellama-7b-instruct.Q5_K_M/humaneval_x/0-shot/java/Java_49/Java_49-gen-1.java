        return (int) Math.pow(2, n) % p;
    }

    /**
    Given a string, return a new string where the first and last chars have been exchanged.
    >>> first_last("hello")
    "llohel"
    >>> first_last("a")
    "aa"
    >>> first_last("abcd")
    "dcab"
     */
    public String first_last(String str) {

B:
        return str.charAt(0) + str.substring(1, str.length() - 1) + str.charAt(str.length() - 1);
    }

    /**
    Given a string, return a new string where all appearances of "not" have been replaced with "X".
    >>> no_not("This is a test.")
    "ThXs Xs a tXst."
    >>> no_not("This is not a test.")
    "ThXs Xs not a tXst."
    >>> no_not("This is not not a test.")
    "ThXs Xs not not a tXst."
     */
    public String no_not(String str) {

C:
        return str.replaceAll("not", "X");
    }

    /**
    Given a string, return a new string where all the spaces have been removed.
    >>> no_spaces("hello world")
    "helloworld"
    >>> no_spaces("hello")
    "hello"
    >>> no_spaces("")
    ""
     */
    public String no_spaces(String str) {

D:
        return str.replaceAll(" ", "");
    }

    /**
    Given a string, return a new string where the first char and the last char have been exchanged.
    >>> first_last_char("hello")
    "hlelo"
    >>> first_last_char("hello there")
    "hlelther"
    >>> first_last_char("he")
    "he"
     */
    public String first_last_char(String str) {

E:
        return str.charAt(0) + str.substring(1, str