// s. trowbridge 2024
#include <iostream>                        
using namespace std;                

int main() { 
    cout << endl;                       

    string name;                                    // declare a string variable (allocate memory)

    cout << "Enter your first and last name: ";     // request data containing a space (a phrase) from the console
    getline(cin, name);                             // store input data into the variable name

    cout << "Your name is " << name << endl;        // print the value of name
    
    cout << endl;  
    return 0;                       
}