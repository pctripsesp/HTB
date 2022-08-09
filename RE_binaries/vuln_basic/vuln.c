#include <string.h>
#include <stdlib.h>
int vuln(char *arg) {
    char buf[256];
    strcpy(buf, arg);
    return 0;
}
int main(int argc, char *argv[]) {
    vuln(argv[1]);
    system("echo executing system function...");
    return 0;
}
