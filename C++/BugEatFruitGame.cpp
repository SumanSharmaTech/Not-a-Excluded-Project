#include <iostream>
#include <conio.h>
#include <windows.h>
using namespace std;

bool gameOver;
const int width = 20; //map dimention
const int height = 20; //map dimention
int x, y, fruitX, fruitY, score;

int tailX[100], tailY[100]; //The tail shall follow the head and prev chracters of body.
int nTail;

enum eDirection { STOP= 0, LEFT, RIGHT, UP, DOWN};   //Enumeration stop,up left right down- w, a, d, s
eDirection dir;

void Setup() //Setups for game
{
    gameOver = false;
    dir = STOP;
    x = width/2; //To center the bug on the map (x)
    y= height/2; //To center the bug on the map (y)
    fruitX = rand() % width; //Place fruit randomly on (x). Random put on width -1 area.
    fruitY = rand() % height; //Place fruit randomly on (x). Random put on width -1 area.
    score = 0;
}

void Draw() //map
{
    system("cls"); //System("clear") to clear screen.
    for (int i = 0; i <width+2; i++) //Map border
        cout << "#"; 
    cout<<endl;

    for (int i = 0; i <height; i++)
    {
        for (int j = 0; j <width; j++)
        {
            if(j == 0)
                cout<<"#";
            if (i == y && j==x)
                cout<<"O";  //Head of the bug
            else if (i == fruitY && j == fruitX)
                cout<<"F"; //Fruit
            else
            {
                bool print = false;
                for(int k = 0; k <nTail; k++) //for making the length of tail.
                {
                    if(tailX[k] == j && tailY[k] == i) //To print tail
                    {
                        cout<< "o";
                        print = true;
                    }
                }
                if (!print)
                    cout<<" ";  //Space 
            }

            if(j == width-1)
                cout<< "#";  //Map border
            
        }
        cout<<endl;
    }
    

    for (int i = 0; i <width+2; i++) //Map border
        cout << "#";

    cout<<endl;
    cout<< "Score: "<< score << endl;

}
void Input() //Controls
{
    if(_kbhit()) //returns a charcter if keyboard is pressed. uses conio.h
    {
        switch(_getch())
        {
            case 'a':
                dir = LEFT;
                break;
            case 'd':
                dir = RIGHT;
                break;
            case 'w':
                dir = UP;
                break;
            case 's':
                dir = DOWN;
                break;
            case 'x':
                gameOver = true;
                break;
        }
    }
}
void Logic()
{
    int prevX = tailX[0]; //prev x coordinate of tail.
    int prevY = tailY[0]; //prev y coordinate of tail.
    int prev2X, prev2Y;
    tailX[0] = x;
    tailY[0] = y;

    for( int i = 1; i < nTail; i++)
    {
        prev2X = tailX[i];
        prev2Y = tailY[i];
        tailX[i]= prevX;
        tailY[i]= prevY;
        prevX = prev2X;
        prevY = prev2Y;

    }

    switch(dir)
    {
        case LEFT:
            x--;
            break;
        case RIGHT:
            x++;
            break;
        case UP:
            y--;
            break;
        case DOWN:
            y++;
            break;
        default:
            break;
    }
    if(x> width || x< 0 || y> height || y< 0) //Hit the wall
        gameOver = true;

    /* Uncomment this to make your bug move through the wall and appear through other side of the wall.
    if(x >= width) x = 0;
    else if (x < 0) x = width -1;

    if(y >= height) y = 0;
    else if (y < 0) y = height -1;
    */

    for(int i = 0; i <nTail; i++)  //Hit the tail
    {
        if(tailX[i] == x && tailY[i] == y)
            gameOver = true;
    }
        
    if(x == fruitX && y == fruitY)
    {
        score += 5;
        fruitX = rand() % width;
        fruitY = rand() % height;
        nTail++;
    }

}
int main()
{
    Setup();
    while (!gameOver)
    {
        Draw();
        Input();
        Logic();
        //Sleep(10); Slows our game. // Uncomment line 3, #include <windows.h>
    }
    return 0;
}

//User's note: The code continously toggels so it's better to open in console window.