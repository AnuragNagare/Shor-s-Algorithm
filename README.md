# Shor-s-Algorithm

Shor's Algorithm Implementation with Qiskit
This repository contains a Python implementation of Shor's algorithm using the Qiskit library. Shor's algorithm is a quantum algorithm for factoring integers efficiently, with potential applications in breaking certain classical cryptographic schemes.

Table of Contents
Introduction
Dependencies
Usage
Results
License

Introduction
Shor's algorithm is a groundbreaking quantum algorithm that can efficiently factor large integers. This implementation showcases the algorithm's core components using the Qiskit library. The code simulates Shor's algorithm for factoring a specified integer n with a chosen integer a.

Dependencies
Before running this code, ensure you have the following dependencies installed:
Python (3.6+)
Qiskit
Tkinter (for the optional GUI)

You can install the required Python packages using pip:
pip install qiskit matplotlib

Usage
Open the shors_algorithm.py file in your preferred Python environment.
Set the values of n (the integer to be factored) and a (a chosen integer less than n) in the code. For example:
n = 15
a = 7

Run the script to execute Shor's algorithm:
python shors_algorithm.py
The code will print the quantum circuit and measurement outcomes to the console.

Optional GUI
To use the GUI for displaying measurement outcomes, make sure you have Tkinter installed:
pip install tk

Run the shors_algorithm_gui.py script to launch the GUI:
python shors_algorithm_gui.py

Click the "Calculate" button in the GUI to execute the algorithm and view the results in a Tkinter window.

Results
The code provides measurement outcomes and displays them either in the console or in a GUI window, depending on your chosen execution method.

Sample output in the console:
Measurement Outcomes:
{'0100': 1}

Sample output in the GUI:
Measurement Outcomes:
{'0100': 1}
