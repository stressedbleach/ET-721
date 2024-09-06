// s. trowbridge 2024
#include <iostream>  
#include <iomanip>              // required for setw() and left/right commands                
using namespace std;                

int main() { 
    cout << endl;                       

    // tab characters may not line up if text data is large
    cout << "Col1\t" << "Col2\t" << "Col3\n";
    cout << "Test\t" << "Test Long String\t" << "Test\n\n";   

    // set(X) creates a column X spaces wide, left aligns all content to the left of the column
    cout << left << setw(10) << "Col1" << setw(20) << "Col2" << "Col3" << "\n";
    cout << left << setw(10) << "Test" << setw(20) << "Test Long String" << "Test" << "\n\n";

    // set(X) creates a column X spaces wide, right aligns all content to the right of the column
    cout << right << setw(10) << "Col1" << setw(20) << "Col2" << setw(10) << "Col3" << "\n";
    cout << right << setw(10) << "Test" << setw(20) << "Test Long String" << setw(10) << "Test" << "\n\n";

    cout << "\n\n";

    cout << endl;  
    return 0;                       
}