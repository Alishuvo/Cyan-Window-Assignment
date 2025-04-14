#include <graphics.h>
#include <conio.h>

int main() {
    // Initialize graphics window
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\Turboc3\\BGI"); // Change path if needed

    // Set background and window title
    setbkcolor(CYAN);
    cleardevice();

    // Set color and draw a simple rectangle to show output
    setcolor(WHITE);
    outtextxy(200, 200, "Press 'S' to exit");

    // Wait for keypress, close on pressing 'S' or 's'
    while (1) {
        char ch = getch();
        if (ch == 'S' || ch == 's') {
            break;
        }
    }

    closegraph();
    return 0;
}

