#include <iostream> // For input/output operations (like cout)
#include <string>   // For using the string data type
#include <vector>   // For using the vector container
#include <iomanip>  // For output formatting (like setw)

// Define the Course structure
struct Course {
    std::string name;       // Name of the course (e.g., "Introduction to Programming")
    std::string id;         // Course ID (e.g., "CS101")
    int credits;            // Number of credits for the course
    std::string instructor; // Name of the instructor
};

// Specialized function to print the details of a single Course object
// Takes a constant reference to a Course object to avoid copying and modification
void printCourseDetails(const Course& course) {
    std::cout << "----------------------------------------" << std::endl;
    std::cout << "Course Name:    " << course.name << std::endl;
    std::cout << "Course ID:      " << course.id << std::endl;
    std::cout << "Credits:        " << course.credits << std::endl;
    std::cout << "Instructor:     " << course.instructor << std::endl;
}

// Function to print details of all courses in a vector
// Takes a constant reference to a vector of Course objects
// Uses an iterator to access each element
void printAllCoursesFromVector(const std::vector<Course>& courses) {
    std::cout << "\nPrinting All Courses from Vector (using iterator):" << std::endl;
    // Declare a constant iterator for the vector of Course objects
    std::vector<Course>::const_iterator it;
    // Loop through the vector using the iterator
    for (it = courses.begin(); it != courses.end(); ++it) {
        // Dereference the iterator to get the Course object
        // and pass it to the printCourseDetails function
        printCourseDetails(*it);
    }
    std::cout << "----------------------------------------" << std::endl;
}

int main() {
    // Create four Course objects
    Course course1 = {"Introduction to C++", "CS101", 3, "Dr. Smith"};
    Course course2 = {"Data Structures", "CS202", 4, "Prof. Jones"};
    Course course3 = {"Algorithms", "CS303", 3, "Dr. Brown"};
    Course course4 = {"Operating Systems", "CS404", 4, "Prof. Davis"};

    // Print the data of the four Course objects using the specialized function
    std::cout << "Printing Individual Course Objects:" << std::endl;
    printCourseDetails(course1);
    printCourseDetails(course2);
    printCourseDetails(course3);
    printCourseDetails(course4);
    std::cout << "----------------------------------------" << std::endl;


    // Create a vector of Course objects
    std::vector<Course> courseCatalog;

    // Add the Course objects to the vector
    courseCatalog.push_back(course1);
    courseCatalog.push_back(course2);
    courseCatalog.push_back(course3);
    courseCatalog.push_back(course4);

    // Print the data from the vector using the function that takes a vector
    // and uses an iterator
    printAllCoursesFromVector(courseCatalog);

    // Alternatively, using a range-based for loop (more modern C++)
    // This is not what was explicitly asked for with the iterator, but good to know.
    std::cout << "\nPrinting All Courses from Vector (using range-based for loop):" << std::endl;
    for (const auto& course : courseCatalog) {
        printCourseDetails(course);
    }
    std::cout << "----------------------------------------" << std::endl;


    return 0; // Indicate successful execution
}

