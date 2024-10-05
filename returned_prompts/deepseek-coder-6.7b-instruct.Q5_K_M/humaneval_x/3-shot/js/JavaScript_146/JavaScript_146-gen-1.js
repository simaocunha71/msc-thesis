  return nums.filter(num => num > 10 && [...(Math.abs(num).toString())].every(d => '13579'.includes(d))).length
}



