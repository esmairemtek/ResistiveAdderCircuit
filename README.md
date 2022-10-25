# ResistiveAdderCircuit

Simulating a resistive adding circuit which has sinusoidal voltage sources with PySpice, and finding the sum of n signals.

We have n sinusoidal signals like Vi(t) = Ai * sin(2π f t), i=1,2,...,n <br />
All the resistors are identical and 1 kOhm <br />
Frequency (f) = 50 Hz for each <br />
Amplitude (Ai) = (3*i-1)V (A1=2V, A2=5V, A3=8V etc.) <br />
We will simulate the circuit and plot V0(t), which we will see that is equal to the average of the signals. <br />
The model of the circuit is down below. <br /> <br />

![Voltage-Summer](https://user-images.githubusercontent.com/76255152/197852348-a89a2d94-d310-425d-9eb5-8f1df08ad32a.gif)

