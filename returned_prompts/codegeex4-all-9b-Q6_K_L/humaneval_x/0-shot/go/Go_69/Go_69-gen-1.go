// The following code is a solution to the problem described above.
func Search(lst []int) int {
  // Create a map to store the frequency of each integer
  freqMap := make(map[int]int)
  // Iterate through the list and update the frequency map
  for _, num := range lst {
    freqMap[num]++
  }
  // Initialize the maximum frequency to -1
  maxFreq := -1
  // Iterate through the frequency map and find the maximum frequency
  for num, freq := range freqMap {
    if freq >= num && freq > maxFreq {
      maxFreq = freq
    }
  }
  // Return the maximum frequency
  return maxFreq
}