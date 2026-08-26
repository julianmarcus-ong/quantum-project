# quantum-project
My first quantum project – running quantum circuits using IBM Quantum Hardware.

# Error-mitigation benchmark
Question: How much do error-mitigation techniques improve QAOA's Max-Cut approximation ratio on real IBM hardware, relative to noiseless and noisy simulation baselines?

# Approach
1. Generate the Max-Cut problem using 6, 9, and 12 nodes - to be solved exactly with a classical solver and stored as fixture
2. Implement the QAOA pipeline (p = 1, 2) with Qiskit primitives, and verify the approximation ratio is ideal on a noiseless simulator
3. Add noisy simulation using a real backend's noise model, and record baseline degradation
4. Implement the mitigation sweep using transpiler optimization levels, dynamical decoupling, twirling, measurement mitigation, and zero noise extrapolation
5. Results harness: one command runs a config matrix and writes the results to a CSV file
6. Execute hardware run(s), log in hardware-log.md

# Deliverables
1. CSV of results
2. Plots comparing techniques
3. Hardware log
4. Final report
## IBM Quantum Open Plan — Free Tier Limits

- Limits: 10 minutes/28 days. Available backends: ibm_fez, ibm_barrakesh, ibm_kingston
- Usage is tracked in `hardware-log.md`

## Working Agreement

- **Demo slot:** Friday evening, 9 PM
- **Definition of done:** A live walkthrough for my sponsor showing the circuit running, the results, and what I learned — not just a finished notebook sitting in the repo.
- **Hard stop:** Week 6 — project wraps regardless of progress at that point
