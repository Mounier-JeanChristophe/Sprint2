#include <iostream>
#include <fstream>
#include <string>
#include<sys/time.h>
#include<algorithm>
using namespace std;

int main(void){
clock_t start, end;
start = clock();
ifstream inFile;
string A;
inFile.open("Boudin-Torres-2006.txt");


if(inFile.fail()){ cerr <<" ERR opening file "<<endl;}

for(int i=0;i<10000;i++){
	(getline(inFile, A));
}
end = clock();
double time_taken = double(end - start) / double(CLOCKS_PER_SEC);
    cout << "Time taken by program is : " 
         << time_taken;
    cout << " sec " << endl;

}
