#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import tkinter as tk
from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram

# Function to create the quantum circuit for Shor's Algorithm
def shors_algorithm(n, a):
    # Initialize quantum and classical registers
    qr = QuantumCircuit(8, 4)
    
    # Apply quantum gates for modular exponentiation
    for i in range(4):
        qr.x(i)
    
    for i in range(4):
        # Controlled modular multiplication by 'a'
        controlled_modular_multiply(qr, a, n, i)
    
    # Apply Quantum Fourier Transform (QFT)
    qr.swap(0, 3)
    for i in range(4):
        qr.h(i)
        for j in range(i + 1, 4):
            qr.swap(i, j)
            angle = 2 * math.pi / (2 ** (j - i))
            controlled_phase_gate(qr, angle, j, i)
    
    # Apply the inverse QFT
    for i in range(4):
        for j in range(i - 1, -1, -1):
            angle = -2 * math.pi / (2 ** (i - j))
            controlled_phase_gate(qr, angle, j, i)
        qr.h(i)
    
    # Measure the first 4 qubits
    qr.measure(range(4), range(4))
    
    return qr

# Controlled modular multiplication by 'a'
def controlled_modular_multiply(qr, a, n, control_qubit):
    for j in range(a):
        angle = 2 * math.pi * (a ** j) / n
        controlled_phase_gate(qr, angle, control_qubit, 4 + (j % 4))

# Controlled-phase gate approximation using rz and cx gates
def controlled_phase_gate(qr, angle, control_qubit, target_qubit):
    qr.rz(angle / 2, target_qubit)
    qr.cx(control_qubit, target_qubit)
    qr.rz(-angle / 2, target_qubit)
    qr.cx(control_qubit, target_qubit)

# Simulate Shor's Algorithm for factoring 15
n = 15
a = 7

quantum_circuit = shors_algorithm(n, a)

# Display the quantum circuit
print("Quantum Circuit:")
print(quantum_circuit)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(quantum_circuit, simulator)
job = assemble(compiled_circuit, shots=1)
result = simulator.run(job).result()

# Display the measurement outcomes
counts = result.get_counts()
print("Measurement Outcomes:")
print(counts)

# Create a function to display the measurement outcomes using tkinter
def display_results():
    # Simulate the circuit
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(quantum_circuit, simulator)
    job = assemble(compiled_circuit, shots=1)
    result = simulator.run(job).result()

    # Get the measurement outcomes
    counts = result.get_counts()

    # Create a tkinter window
    root = tk.Tk()
    root.title("Shor's Algorithm Results")

    # Create a tkinter label to display the measurement outcomes
    label = tk.Label(root, text="Measurement Outcomes:")
    label.pack()

    # Create a tkinter text widget to display the counts
    text_widget = tk.Text(root)
    text_widget.pack()

    # Insert the measurement outcomes into the text widget
    text_widget.insert(tk.END, str(counts))

    # Start the tkinter main loop
    root.mainloop()

# Create a tkinter button to trigger the calculation and display
root = tk.Tk()
root.title("Shor's Algorithm")

calculate_button = tk.Button(root, text="Calculate", command=display_results)
calculate_button.pack()

root.mainloop()


# In[ ]:




