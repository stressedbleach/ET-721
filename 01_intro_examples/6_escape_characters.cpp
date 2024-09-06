// s. trowbridge 2024
#include <iostream>                 
using namespace std;                

int main() {  
    cout << endl;                         

    cout << "Hello World" << endl;  // endline to move to the next line
    cout << "Hello World\n";        // newline escape character to move to the next line 
    cout << "\n\n";                 // multiple newline escape characters to move two lines

    cout << "Hello World\n";
    cout << "Hello\tWorld\n";       // tab escape character to indent
    cout << "Hello\t\tWorld\n\n";   // multiple tab characters to indent multiple times

    cout << endl;      
    return 0;                       
}