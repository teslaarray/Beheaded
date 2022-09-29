#include <iostream>

using namespace std;

int data[] = {1, 2, 3};

int *lol()
{
    return &data[1];
}

void test(int *const &x)
{
    *x = 30;
}

void t1(int &a)
{
    a = 50;
}

int main()
{
    test(&data[1]);
    cout << data[1] << endl;
    *lol() = 10;
    cout << data[1] << endl;

    t1(data[1]);
    cout << data[1] << endl;
}