
// Circular shift the digits of the integer x, shift the digits right by shift
// and return the result as a string.
// If shift > number of digits, return digits reversed.
// >>> CircularShift(12, 1)
// "21"
// >>> CircularShift(12, 2)
// "12"
func CircularShift(x int,shift int) string {
    if x == 0 {
        return ""
    } else{
      shift %= len(strconv.Itoa(int64(x))) + 1 // + 1 so that we include the last digit in the shift
      
      var r string
      for i := range (strconv.Itoa(int64(x)))-shift {
         if i == strconv.Itoa(int64(x)) - shift {
             break
          } else {
            r += "0"
         }
       }  
      return r + strconv.Itoa(int64(x))[strconv.Itoa(int64(x))-shift:]
    }
}
