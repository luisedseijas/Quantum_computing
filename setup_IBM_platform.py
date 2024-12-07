token = "**********"

from qiskit_ibm_runtime import QiskitRuntimeService

QiskitRuntimeService.save_account(
    token= token, 
    channel="ibm_quantum",
    overwrite=True
)