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
    for i in range(8):
        for j in range(i + 1, 8):
            v = np.zeros(8)
            v[i], v[j] = 1, 1
            vertices.append(v)
            vertices.append(-v)
    for s in [(1, 1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, -1, -1, -1, -1)]:
        v = np.array(s) / 2
        vertices.append(v)
        vertices.append(-v)
    return np.array(vertices)[:num_vertices] * phi

def project_to_3d(vertices, window_size=2.0):
    """Proyecta vértices de 8D a 3D usando cut-and-project."""
    projection_matrix = np.random.randn(3, 8)
    projection_matrix = np.linalg.qr(projection_matrix.T)[0].T  # Ortogonalizar
    projected = np.dot(vertices, projection_matrix.T)  # (20,8) @ (8,3) = (20,3)
    window = np.sum(projected**2, axis=1) < window_size**2
    return projected[window]

def generate_hexagonal_grid(radius=0.3, num_rings=2):
    """Genera una rejilla hexagonal para la Flor de la Vida."""
    phi = (1 + np.sqrt(5)) / 2  # Escalar con proporción áurea
    centers = [(0, 0)]  # Centro del patrón
    for ring in range(1, num_rings + 1):
        for i in range(6):
            angle = i * np.pi / 3  # 60 grados entre vecinos
            x = ring * radius * np.cos(angle) * phi
            y = ring * radius * np.sin(angle) * phi
            centers.append((x, y))
    return np.array(centers)

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

def plot_flower_of_life(ax2d, centers, radius=0.3):
    """Dibuja la Flor de la Vida con círculos entrelazados."""
    for center in centers:
        circle = plt.Circle(center, radius, color='r', alpha=0.2)
        ax2d.add_patch(circle)

def create_correlation_circuit(num_qubits, interactions):
    """Crea un circuito cuántico con correlaciones entrelazadas."""
    qc = QuantumCircuit(num_qubits)
    for i in range(num_qubits):
        qc.h(i)  # Superposición
    for i, j in interactions:
        qc.rzz(0.5, i, j)  # Correlaciones Ising
        qc.cx(i, j)  # Entrelazamiento
    qc.measure_all()
    return qc

# Generar vértices y proyectar
e8_vertices = generate_e8_vertices(num_vertices=20)
points_3d = project_to_3d(e8_vertices, window_size=2.0)
points, simplices = generate_tetrahedra(points_3d)

# Generar rejilla hexagonal para la Flor de la Vida
radius = 0.3
centers_2d = generate_hexagonal_grid(radius=radius, num_rings=2)

# Mapear puntos a qubits
num_qubits = min(len(points), 10)
interactions = [(i, (i+1)%num_qubits) for i in range(num_qubits)]
qc = create_correlation_circuit(num_qubits, interactions)

# Simular en AerSimulator
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

# Visualización
fig = plt.figure(figsize=(15, 7))
ax = fig.add_subplot(121, projection='3d')
plot_tetrahedra(ax, points, simplices)
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("E8-Derived Quasicrystal (QSN)")

# Subgráfico 2D para la Flor de la Vida
ax2d = fig.add_subplot(122)
plot_flower_of_life(ax2d, centers_2d, radius=radius)
ax2d.set_xlim([-1, 1])
ax2d.set_ylim([-1, 1])
ax2d.set_xlabel('X')
ax2d.set_ylabel('Y')
ax2d.set_title("Holographic Flower of Life (Hexagonal)")
ax2d.set_aspect('equal')

# Texto explicativo
text = (
    "E8, QSN, Flower of Life, and Holographic Correlations\n\n"
    "This simulation projects the E8 lattice (8D) to a 3D quasicrystal (QSN) and a 2D Flower of Life. "
    "Tetrahedra are mapped to qubits, with entangled correlations (Ising + CNOT) modeling the universe as correlations, not particles. "
    "The E8's Gosset polytope (240 vertices) encodes interactions via symmetries. The QSN models physics at Planck scale (10^44 frames per second). "
    "The Flower of Life, with hexagonal/golden ratio symmetries, is a 2D holographic projection encoding 4D correlations, "
    "governing forms like DNA and crystals on Earth.\n\n"
    "This '5D printer' envisions E8/QSN generating universes via correlations, with the Flower of Life as a 2D holographic signature."
)
fig.text(0.1, 0.02, text, fontsize=8, bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))

plt.show()

# Imprimir resultados cuánticos
print("Quantum simulation results:", counts)
