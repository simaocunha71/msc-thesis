	// A car has two possible directions: left to right and right to left.
	// In the beginning, the left to right cars are all at position 0 and
	// the right to left cars are all at position n.
	int left_to_right[n], right_to_left[n];
	for(int i=0; i<n; i++) {
		left_to_right[i] = 0;
		right_to_left[n-1-i] = n;
	}

	int left_to_right_index = 0;
	int right_to_left_index = n-1;

	int collision = 0;
	while(1) {
		// Move left to right cars.
		if(left_to_right_index < n) {
			left_to_right[left_to_right_index]++;
			left_to_right_index++;
		} else {
			collision += right_to_left[right_to_left_index];
			right_to_left_index--;
			if(right_to_left_index < 0) break;
		}

		// Move right to left cars.
		if(right_to_left_index >= 0) {
			right_to_left[right_to_left_index]++;
			right_to_left_index--;
		} else {
			collision += left_to_right[left_to_right_index];
			left_to_right_index++;
			if(left_to_right_index >= n) break;
		}
	}

	return collision;
}

int main(){
	int n;
	scanf("%d", &n);
	printf("%d\n", car_race_collision(n));
	return 0;
}
