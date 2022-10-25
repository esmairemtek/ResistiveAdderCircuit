import PySpice
import numpy as np
import matplotlib.pyplot as plt
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

# We have three n signals like Vi(t) = Ai * sin(2π f t), i=1,2,...,n
# All the resistors are identical and 1 kOhm
# Frequency (f) = 50 Hz for each
# Amplitude (Ai) = (3*i-1)V (A1=2V, A2=5V, A3=8V etc.)
# We will simulate the circuit and plot V0(t), which we will see that is equal to the average of the signals.

circuit = Circuit("Resistive Adder")

numberOfSignals = int(input("Enter the number of signals in the resistive adder circuit: "))

i = 1
while (i <= numberOfSignals): # adding sources and resistors to the circuit
    circuit.SinusoidalVoltageSource(i, i, circuit.gnd, amplitude=(3*i-1)@u_V, frequency=50@u_Hz)
    circuit.R(i, str(i), "V_end", 1@u_kOhm)
    i += 1
    
    
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.transient(step_time=100@u_us, end_time=100@u_ms)

fig = plt.figure()

i = 1
while(i <= numberOfSignals): # adding voltages to the chart
    plt.plot(np.array(analysis.time), np.array(analysis[str(i)]), label=("V", str(i)))
    i += 1
    
plt.plot(np.array(analysis.time), np.array(analysis["V_end"]), label=("V_end"))

plt.legend()
plt.xlabel("Time")
plt.ylabel("Voltage")
