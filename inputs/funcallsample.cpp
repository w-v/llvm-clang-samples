#include <iostream>
bool foo()
{
    return true;
}

void bar()
{
    foo();
    for (int i = 0; i < 10; ++i)
        foo();
}

int main()
{
  std::cout << "hu"<< std::endl;
    bar();
    if (foo())
        bar();
}
