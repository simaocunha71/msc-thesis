It's a bug in Go 1.2. The implementation of the IsPalindrome function in the godoc is incorrect. It should return true for the string "cata".

Here's a test that shows the bug:

```
func TestMakePalindrome(t *testing.T) {
    t.Run("MakePalindrome('')", func(t *testing.T) {
        if MakePalindrome("") != "" {
            t.Fatal("MakePalindrome('') != ''")
        }
    })
    t.Run("MakePalindrome('cat')", func(t *testing.T) {
        if MakePalindrome("cat") != "catac" {
            t.Fatal("MakePalindrome('cat') != 'catac'")
        }
    })
    t.Run("MakePalindrome('cata')", func(t *testing.T) {
        if MakePalindrome("cata") != "catac" {
            t.Fatal("MakePalindrome('cata') != 'catac'")
        }
    })
}
```
