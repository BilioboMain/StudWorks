#include <iostream>
#include <stdio.h>
#include <math.h>
#include "NewDouble.h"

DoubleNum operator+(DoubleNum a, DoubleNum b) {
	int exp_2,mant_2;

	while (a.exp > b.exp) {
		a.exp--;
		a.mant *= 2;
	}
	while (b.exp > a.exp)
	{
		b.exp--;
		b.mant *= 2;
	}
	exp_2 = b.exp;
	mant_2 = b.mant + a.mant;
	DoubleNum result(exp_2, mant_2);
	return result;
}

DoubleNum operator-(DoubleNum a, DoubleNum b) {
	int exp_2, mant_2;
	while (a.exp > b.exp) {
		a.exp--;
		a.mant *= 2;
	}
	while (b.exp > a.exp)
	{
		b.exp--;
		b.mant *= 2;
	}

	mant_2 = a.mant - b.mant;
	exp_2 = a.exp;
	DoubleNum result(exp_2, mant_2);
	return result;
}

DoubleNum operator*(DoubleNum a, DoubleNum b) {
	int mant_2, exp_2;
	mant_2 = a.mant * b.mant;
	exp_2 = a.exp + b.exp;
	DoubleNum result(exp_2, mant_2);
	return result;
}

DoubleNum operator/(DoubleNum a, DoubleNum b) {
	int exp_2, mant_2;
	mant_2 = (a.mant * 1024) / b.mant;
	exp_2 = a.exp - b.exp - 10;
	DoubleNum result(exp_2, mant_2);
	return result;
}