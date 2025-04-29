#include <iostream>
#include <vector>
#include <string>

using namespace std;

void displayMenu() {
    cout << "===== To-Do List Menu =====" << endl;
    cout << "1. Add Task" << endl;
    cout << "2. View Tasks" << endl;
    cout << "3. Remove Task" << endl;
    cout << "4. Exit" << endl;
    cout << "===========================" << endl;
}

void addTask(vector<string>& tasks) {
    string task;
    cout << "Enter the task: ";
    cin.ignore(); // To clear the input buffer
    getline(cin, task);
    tasks.push_back(task);
    cout << "Task added successfully!" << endl;
}

void viewTasks(const vector<string>& tasks) {
    if (tasks.empty()) {
        cout << "No tasks in the list!" << endl;
        return;
    }

    cout << "===== To-Do List =====" << endl;
    for (size_t i = 0; i < tasks.size(); ++i) {
        cout << i + 1 << ". " << tasks[i] << endl;
    }
    cout << "======================" << endl;
}

void removeTask(vector<string>& tasks) {
    if (tasks.empty()) {
        cout << "No tasks to remove!" << endl;
        return;
    }

    int taskNumber;
    cout << "Enter the task number to remove: ";
    cin >> taskNumber;

    if (taskNumber < 1 || taskNumber > static_cast<int>(tasks.size())) {
        cout << "Invalid task number!" << endl;
    } else {
        tasks.erase(tasks.begin() + taskNumber - 1);
        cout << "Task removed successfully!" << endl;
    }
}

int main() {
    vector<string> tasks;
    int choice;

    while (true) {
        displayMenu();
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                addTask(tasks);
                break;
            case 2:
                viewTasks(tasks);
                break;
            case 3:
                removeTask(tasks);
                break;
            case 4:
                cout << "Exiting the program. Goodbye!" << endl;
                return 0;
            default:
                cout << "Invalid choice! Please try again." << endl;
        }

        cout << endl; // Add a blank line for better readability
    }

    return 0;
}
