CC = g++
FLAGS = --std=c++11
EXEC = solver

all:
	@echo "Building solver..."
	$(CC) $(FLAGS) dpll.c -o $(EXEC)
	@echo "Done."
parallel:
	@echo "Building parallel solver..."
	$(CC) $(FLAGS) solver.cpp -fopenmp -o $(EXEC)
	@echo "Done."

run-stat:
	@echo "Building stat benchmarks..."
	$(CC) $(FLAGS) run_tests.cpp -o run_tests
	@echo "Done."	

clean:
	@echo "Cleaning up..."
	rm $(EXEC)
	@echo "Done."
