
// if the need is less than or equal to the remaining carrots, then just add the number to the need
if need <= remaining {
	return []int{number + need, remaining - need}
}

// if the need is greater than the remaining carrots, then add the number to the need, and subtract the remaining from the need
return []int{number + need, 0}

}


