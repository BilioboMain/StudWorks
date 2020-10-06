
using namespace std;
#include <iostream>
#include <math.h>
#include <stdio.h>

class DoubleNum {
protected: int mant,exp, pm;
public:

	DoubleNum(double NUM) {
		mant = 0;
		exp = 0;
		pm = 0;
		if (NUM < 0) {
			pm = 1;
		}
		if (NUM != 0) {
			while (abs(NUM) < 0.5)
			{
				NUM *= 2;
				exp--;
			}
			while (abs(NUM) > 1)
			{
				NUM /= 2;
				exp++;
			}
			mant = int(NUM * 1024);
			exp -= 10;
		}
	}
	DoubleNum(int newExp, int newMant) {
		mant = 0;
		exp = 0;
		pm = 0;
		mant = newMant;
		exp = newExp;
		while (abs(mant) < 512) { mant *= 2; exp--; }
		while (abs(mant) > 1024) { mant /= 2; exp++; }
	}
	void print() {
		printf("%f [%d,%d] ", mant * pow(2.0, double(exp)), mant, exp);
	}
	friend DoubleNum operator+(DoubleNum, DoubleNum);
	friend DoubleNum operator-(DoubleNum, DoubleNum);
	friend DoubleNum operator/(DoubleNum, DoubleNum);
	friend DoubleNum operator*(DoubleNum, DoubleNum);
};


 

