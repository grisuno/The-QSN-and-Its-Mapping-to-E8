import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.spatial import Delaunay
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Operator

def generate_e8_vertices(num_vertices=20):
    """Genera un subconjunto de vértices del E8 en 8D."""
    phi = (1 + np.sqrt(5)) / 2  # Proporción áurea
    vertices = []
    # Vértices tipo (±1, ±1, 0, 0, 0, 0, 0, 0) y permutaciones
    for i in range(8):
        for j in range(i + 1, 8):
            v = np.zeros(8)
            v[i], v[j] = 1, 1
            vertices.append(v)
            vertices.append(-v)
    # Vértices tipo (±1/2, ±1/2, ±1/2, ±1/2, ±1/2, ±1/2, ±1/2, ±1/2)
    for s in [(1, 1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, -1, -1, -1, -1)]:
        v = np.array(s) / 2
        vertices.append(v)
        vertices.append(-v)
    return np.array(vertices)[:num_vertices] * phi

def project_to_3d(vertices, window_size=2.0):
    """Proyecta vértices de 8D a 3D usando cut-and-project."""
    # Matriz de proyección 8D -> 3D (simplificada, idealmente ortogonal)
    projection_matrix = np.random.randn(3, 8)
    projection_matrix /= np.linalg.norm(projection_matrix, axis=1)[:, None]
    projected = np.dot(vertices, projection_matrix.T)
    # Ventana de corte: puntos dentro de un cubo
    window = np.sum(projected**2, axis=1) < window_size**2
    return projected[window]

def generate_tetrahedra(points):
    """Genera tetraedros usando triangulación de Delaunay."""
    try:
        tri = Delaunay(points)
        return tri.points, tri.simplices
    except Exception as e:
        print(f"Error en Delaunay: {e}")
        return points, []

def plot_tetrahedra(ax, points, simplices, color='b'):
    """Visualiza tetraedros en 3D."""
    for simplex in simplices:
        x = points[simplex, 0]
        y = points[simplex, 1]
        z = points[simplex, 2]
        ax.plot_trisurf(x, y, z, color=color, alpha=0.3)

def create_ising_circuit(num_qubits, interactions):
    """Crea un circuito cuántico para un modelo de Ising simplificado."""
    qc = QuantumCircuit(num_qubits)
    # Estado inicial: superposición
    for i in range(num_qubits):
        qc.h(i)
    # Interacciones tipo Ising (ZZ)
    for i, j in interactions:
        qc.rzz(0.5, i, j)  # Puerta RZZ para interacción
    # Medición
    qc.measure_all()
    return qc

# Generar vértices y proyectar
e8_vertices = generate_e8_vertices(num_vertices=20)
points_3d = project_to_3d(e8_vertices, window_size=2.0)
points, simplices = generate_tetrahedra(points_3d)

# Mapear puntos a qubits (limitado a 10 qubits para simulación)
num_qubits = min(len(points), 10)
interactions = [(i, (i+1)%num_qubits) for i in range(num_qubits)]
qc = create_ising_circuit(num_qubits, interactions)

# Simular en AerSimulator
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

# Visualización
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')
plot_tetrahedra(ax, points, simplices)
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("E8-Derived Quasicrystal with Qiskit Simulation")

# Texto explicativo
text = (
    "QSN and E8 Quantum Simulation\n\n"
    "This simulation projects the E8 lattice (8D) to a 3D quasicrystal, representing the QSN. "
    "Tetrahedra are mapped to qubits in a Qiskit circuit, simulating interactions via an Ising model. "
    "The E8's Gosset polytope (240 vertices) may encode particles and forces. "
    "The QSN models physics at Planck scale, with tetrahedra changing states at 10^44 frames per second, "
    "potentially forming particles and laws.\n\n"
    "This '5D printer' concept envisions the QSN generating universes from E8 projections, "
    "simulated here with Qiskit."
)
ax.text(2.5, 2.5, 2.5, text, fontsize=8, bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))

plt.show()

# Imprimir resultados cuánticos
print("Quantum simulation results:", counts)
