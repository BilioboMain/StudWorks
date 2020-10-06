
#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;

class ChildDouble : public DoubleNum {
protected: int flag;
public:

	ChildDouble(DoubleNum n) : DoubleNum(n) {
		flag = 0;
		if (mant * pow(2.0, double(exp))>16384) {
			exp = 4;
			mant = 1024;
			flag = 1;
		}
	}
	void print() {
		printf("%f [%d,%d,%d] ", mant * pow(2.0, double(exp)), mant, exp, flag);
	}
};