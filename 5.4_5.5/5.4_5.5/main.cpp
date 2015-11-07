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
//	ifstream inFile("/Users/MinhTri/Projects/NLP_5455/traindataset_DonaldTrump_300_OpinionatedWords.csv");
//	ofstream outRefined("/Users/MinhTri/Projects/NLP_5455/300words.arff");
//	string line;
//	int counter = 0;
//	while (getline(inFile, line)) {
////		if (counter > 400) break;
//		outRefined << line << endl;
//		counter ++;
//	}
	
	
	ifstream inFile("/Users/MinhTri/Projects/NLP_5455/300words.arff");
	ofstream outS1("/Users/MinhTri/Projects/NLP_5455/set1.arff");
	ofstream outS2("/Users/MinhTri/Projects/NLP_5455/set2.arff");
	ofstream outS3("/Users/MinhTri/Projects/NLP_5455/set3.arff");
	ofstream outS12("/Users/MinhTri/Projects/NLP_5455/set12.arff");
	ofstream outS23("/Users/MinhTri/Projects/NLP_5455/set23.arff");
	ofstream outS13("/Users/MinhTri/Projects/NLP_5455/set13.arff");
	string line;
	int counter = 0;
	while (getline(inFile, line)) {
		if (line.size() < 5) continue;
		if (line[0] != '\"' && line[0] != '@') {
//			cout << line << endl;
//			cout << line.size() - 1 << endl;
//			cout << line.substr(line.size() - 1, 1) << endl;
			string ans = line.substr(line.size() - 1, 1);
			line = line.substr(0, line.size() - 2);
			line = "\"" + line + "\"" + "," + ans;
//			cout << line << endl;
		}
		if (line[0] == '\"') {
			//			cout << line << endl;
			//			cout << line.size() - 1 << endl;
			//			cout << line.substr(line.size() - 1, 1) << endl;
			string ans = line.substr(line.size() - 1, 1);
			line = line.substr(1, line.size() - 4);
			for(int i = 0; i < line.size(); i ++)
				if (line[i] == '\"') line[i] = '\'';
			line = "\"" + line + "\"" + "," + ans;
			//			cout << line << endl;
		}
		if (counter > 400) break;
		if (counter < 7) {
			outS1 << line << endl;
			outS2 << line << endl;
			outS3 << line << endl;
			outS12 << line << endl;
			outS13 << line << endl;
			outS23 << line << endl;
		}
		if (counter > 7) {
			if ((counter - 7) % 3 == 0) {
				outS1 << line << endl;
				outS13 << line << endl;
				outS12 << line << endl;
			}
			if ((counter - 7) % 3 == 1) {
				outS2 << line << endl;
				outS23 << line << endl;
				outS12 << line << endl;
			}
			if ((counter - 7) % 3 == 2) {
				outS3 << line << endl;
				outS13 << line << endl;
				outS23 << line << endl;
			}
		}
		counter ++;
	}
    return 0;
}
