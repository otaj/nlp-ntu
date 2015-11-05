//
//  main.cpp
//  NLP_5455
//
//  Created by Minh Tri Tran on 6/11/15.
//  Copyright (c) 2015 Minh Tri Tran. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, const char * argv[]) {
	ifstream inFile("/Users/MinhTri/Projects/NLP_5455/labelled.arff");
	ofstream outS1("/Users/MinhTri/Projects/NLP_5455/set1.arff");
	ofstream outS2("/Users/MinhTri/Projects/NLP_5455/set2.arff");
	ofstream outS3("/Users/MinhTri/Projects/NLP_5455/set3.arff");
	ofstream outS12("/Users/MinhTri/Projects/NLP_5455/set12.arff");
	ofstream outS23("/Users/MinhTri/Projects/NLP_5455/set23.arff");
	ofstream outS13("/Users/MinhTri/Projects/NLP_5455/set13.arff");
	string line;
	int counter = 0;
	while (getline(inFile, line)) {
		if (counter > 400) break;
		if (counter < 8) {
			outS1 << line << endl;
			outS2 << line << endl;
			outS3 << line << endl;
			outS12 << line << endl;
			outS13 << line << endl;
			outS23 << line << endl;
		}
		if (8 <= counter && counter < 108) {
			outS1 << line << endl;
			outS13 << line << endl;
			outS12 << line << endl;
		}
		if (108 <= counter && counter < 208) {
			outS2 << line << endl;
			outS23 << line << endl;
			outS12 << line << endl;
		}
		if (208 <= counter && counter < 308) {
			outS3 << line << endl;
			outS13 << line << endl;
			outS23 << line << endl;
		}
		counter ++;
	}
    return 0;
}
