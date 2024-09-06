// s. trowbridge 2024
#include <iostream>                        
using namespace std;                

int main() { 
    cout << endl;                       

    string name;                                // declare a string variable (allocate memory)

    cout << "Enter your name: ";                // request data from the console
    cin >> name;                                // store input data into the variable name (what happens if you enter two names?)

    cout << "Your name is " << name << endl;    // print the value of name
    
    cout << endl;  
    return 0;                       
}