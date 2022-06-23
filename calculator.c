#include <stdio.h>


// GLOBAL VARIABLES
int x1;
int x2;
char operator;
int result;


// CALCULATOR FUNCTIONS

// add
// 	- x , y : integer input parameters 
//	- return: sum of x & y
int add(int x, int y) {
	int sum = x + y;
	return sum;
}

// subtract
// TODO

// multiply
// TODO

// divide
// TODO



// CALCULATE DECISION FUNCTION
//	- NULL: input parameters
//	- return NULL (a.k.a nothing)
void calculate() {
	if (operator == '+') {
		result = add(x1, x2);
	}

	// TODO continue...
}



// USER INPUT FUNCTION
//	- NULL: input parameters
//	- return NULL (a.k.a nothing)
void get_input() {
	printf("Enter x1  +/-*  x2: ");
	scanf("%d %c %d", &x1, &operator, &x2);
}



// MAIN FUNCTION
int main() {
	get_input();

	calculate();

	printf("%d %c %d = %d\n", x1, operator, x2, result);

	return 0;
}





