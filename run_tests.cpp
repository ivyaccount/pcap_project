#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <dirent.h>

// Function to execute perf stat command for a given test file
void executePerfStat(const std::string& testFileName, std::ofstream& outputFile) {
    std::string command = "perf stat ./solver < " + testFileName + " 2>&1"; // Redirect stderr to stdout

    std::cout << "Executing command: " << command << std::endl;

    FILE* perfProcess = popen(command.c_str(), "r");
    if (!perfProcess) {
        std::cerr << "Error executing perf stat command for " << testFileName << std::endl;
        return;
    }

    std::stringstream output;
    char buffer[128];
    while (fgets(buffer, sizeof(buffer), perfProcess) != nullptr) {
        output << buffer;
    }
    pclose(perfProcess);

    // Write perf stat output to the single output file
    outputFile << "=== Output for test file: " << testFileName << " ===\n";
    outputFile << output.str() << "\n\n";
}

int main() {
    // Directory containing test files
    std::string testFilesDir = "file-dimacs-aim/"; // Replace with your directory path

    // Open a single output file to store all the perf stat outputs
    std::ofstream outputLogFile("perf_output_log.txt");
    if (!outputLogFile.is_open()) {
        std::cerr << "Error opening output log file." << std::endl;
        return 1;
    }

    DIR* dir;
    struct dirent* ent;
    if ((dir = opendir(testFilesDir.c_str())) != nullptr) {
        while ((ent = readdir(dir)) != nullptr) {
            std::string fileName = ent->d_name;
            if (fileName != "." && fileName != "..") {
                std::string filePath = testFilesDir + fileName;
                executePerfStat(filePath, outputLogFile);
            }
        }
        closedir(dir);
    } else {
        std::cerr << "Error opening directory: " << testFilesDir << std::endl;
        return 1;
    }

    outputLogFile.close();
    std::cout << "All perf stat outputs have been written to perf_output_log.txt" << std::endl;

    return 0;
}
