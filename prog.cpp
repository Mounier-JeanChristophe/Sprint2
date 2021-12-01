#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(void){

ifstream inFile;
ofstream outFile;
string maChaine2 ="Abstract";
string maChaine1 ="<title>";
string title;
string abstract;
string ligne;
string str, result;
string stop1 = "1";
bool verif = true;
inFile.open("Boudin-Torres-2006.html"); //input
if(inFile.fail()){ 
	cerr <<" ERR opening file "<<endl;
	exit(1);
}
outFile.open("out.txt", ios::out | ios::trunc); //output
while(getline(inFile, ligne)){
	if(ligne.find(maChaine1) != string::npos){
		std::size_t pos = ligne.find("<title>");
		str = ligne.substr (pos+7);	
		std::size_t pos2 = str.find("</title>");
		title = str.substr (0,pos2);
		//cout <<title<<endl;
		break;
	}
}

while(getline(inFile, ligne)){
	if(ligne.find(maChaine2) != string::npos){
	getline(inFile, ligne);
	while(verif == true){
	std::size_t pos = ligne.find("<word");
	str = ligne.substr (pos+76);
	std::size_t pos2 = str.find("</word>");
	abstract = str.substr (0,pos2);
	if(abstract.find(stop1) != string::npos){
			verif = false;		
	}
	else{
		std::size_t pos = ligne.find(">");
		str = ligne.substr (pos+1);
		std::size_t pos2 = str.find("</word>");
		abstract = str.substr (0,pos2);
		result = result + abstract + " ";
		getline(inFile, ligne);
	}
	
	
	
	
	}
	
}

}
if(outFile.is_open()) {
     outFile << "Boudin-Torres-2006.html"<<endl;
     outFile << title <<endl;
     outFile << result;
}

inFile.close();
outFile.close();
}
