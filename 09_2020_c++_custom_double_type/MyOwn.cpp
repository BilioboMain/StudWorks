
#include <iostream>
#include <math.h>
#include"NewDouble.h"
#include"ChildDouble.h"
#include<stdio.h>
using namespace std;
int main()
{
	double n, n2;
	n = 17000;
	n2 = 1000;
	DoubleNum Num(n);
	DoubleNum num2(n2);
	//Num.print();
	//num2.print();
	//DoubleNum res(Num / num2);

	ChildDouble result(Num*num2);
	ChildDouble newNum(Num);
	ChildDouble newnum2(num2);
	newNum.print();
	newnum2.print();
	result.print();
}
