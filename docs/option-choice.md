# Introduction: Error mitigation benchmark

This is my first quantum computing project.

To start, I was given a choice of three options:
1. Error-mitigation benchmark
2. Quantum machine learning showdown
3. Backend weather report

I decided to pick the first option as I was more familiar with the quantum approximate optimization algorithm (QAOA) than the other two choices. By taking part in the IBM Quantum Road to Practitioner Program (R2P), I was introduced to a number of algorithms including the QAOA, and the Max-Cut problem. However, I am not familiar with error suppression and mitigation, which includes zero-noise extrapolation, twirling, and dynamical decoupling.

For reference, I looked at the tutorial provided by IBM, and I am familiar with the estimator, and the fact it uses a cost function.
https://quantum.cloud.ibm.com/docs/en/tutorials/quantum-approximate-optimization-algorithm

The tutorial uses the QAOA algorithm used to solve the Max-Cut problem on a 5-node and a 100-node graph.

## Risks
 One risk of this project is the Open Plan only allows 10 minutes per 28 days, and the estimate that the tutorial gives is 22 minutes on a Heron r3 processor. Another risk is that job mode is the only mode available to Open Plan users, and the tutorial relies on session mode, meaning I will have to rely on the queue to execute tasks.

## Next steps
To begin, I will generate the Max-Cut problem using 6, 9, and 12 nodes, and solve using a classical solver. Afterwards, I will implement QAOA pipeline with Qiskit primitives and verify the approximation ratio, which should be ideal on a noiseless simulation.
I will also add a noisy simulation using the real backend's noise model, then implement the mitigation sweep which includes transpiler optimization levels, twirling, and dynamical decoupling.