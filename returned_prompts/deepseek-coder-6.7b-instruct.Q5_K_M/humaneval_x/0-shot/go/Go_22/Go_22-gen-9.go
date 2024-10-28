
	result := make([]map[string]interface{}, 0)
	for _, value := range values {
		if val, ok := value.(map[string]interface{}); ok {
			result = append(result, val)
		}
	}
	return result
}

// Filter given list of any