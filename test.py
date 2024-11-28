# Load saved credentials
service = QiskitRuntimeService()

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

# Crear un circuito vacio
example_circuit = QuantumCircuit(2)
example_circuit.measure_all()

service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)     

sampler = Sampler(backend)
job = sampler.run_circuits([example_circuit], shots=1000)
print(f"job id: {job.job_id()}") 
result = job.result()
print(result)   