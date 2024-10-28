	int counter = 0;
	for (int i = 0; i < file_name.size(); i++) {
		if (file_name[i] >= 48 && file_name[i] <= 57) {
			counter++;
		}
	}
	if (counter > 3) {
		return "No";
	}
	int counter2 = 0;
	int counter3 = 0;
	for (int i = 0; i < file_name.size(); i++) {
		if (file_name[i] >= 97 && file_name[i] <= 122) {
			counter2++;
		}
		if (file_name[i] >= 65 && file_name[i] <= 90) {
			counter3++;
		}
	}
	if (counter2 == 0 || counter3 == 0) {
		return "No";
	}
	int counter4 = 0;
	for (int i = 0; i < file_name.size(); i++) {
		if (file_name[i] == '.') {
			counter4++;
		}
	}
	if (counter4 != 1) {
		return "No";
	}
	string ext = "";
	int j = file_name.size() - 1;
	while (j >= 0) {
		if (file_name[j] == '.' || file_name[j] == ' ') {
			break;
		}
		else {
			ext += file_name[j];
		}
		j--;
	}
	if (ext != "txt" && ext != "dll" && ext != "exe") {
		return "No";
	}
	return "Yes";
}

























































