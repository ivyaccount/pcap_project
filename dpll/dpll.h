#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Literal {
  struct Literal * next; // points to the next literal in the clause
  int index;
};

struct Clause {
  struct Literal * head; // points to the first literal in the clause
  struct Clause * next; // points to the next clause in the set
};