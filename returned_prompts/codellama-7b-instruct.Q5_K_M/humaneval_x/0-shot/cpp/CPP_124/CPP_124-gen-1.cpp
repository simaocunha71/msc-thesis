	return true;
}

int main(){
	string date = "02-12-2020";
	bool result = valid_date(date);
	if(result == true)
		printf("Valid");
	else
		printf("Invalid");
	return 0;
}

