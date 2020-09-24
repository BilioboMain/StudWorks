
#include <iostream>
#include <math.h>
#include"Header1.h"
#include<stdio.h>
using namespace std;
int main()
{
	double n,n2;
	n = -6;
	n2 = -5;
	DoubleNum Num(n);
	DoubleNum num2(n2);
	Num.print();
	num2.print();
	DoubleNum res(Num / num2);
	res.print();
}
