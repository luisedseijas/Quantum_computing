token = "11aa3ba1ed9053bcbb436c2f273c333b741de09122c9977700f445ca4507520eb7368d3df689f6c6eef304abeec32f51f0f4c7abcf59d72429865d9b7a0b59e6"

from qiskit_ibm_runtime import QiskitRuntimeService

QiskitRuntimeService.save_account(
    token= token, 
    channel="ibm_quantum",
    overwrite=True
)