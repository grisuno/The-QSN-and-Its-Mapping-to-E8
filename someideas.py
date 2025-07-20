import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.spatial import Delaunay

def generate_e8_vertices():
    """Genera un subconjunto de vértices del E8 (Gosset polytope) en 8D."""
    # Subconjunto simplificado de vértices del E8 (240 vértices son complejos, usamos una aproximación)
    phi = (1 + np.sqrt(5)) / 2  # Proporción áurea para simetrías cuasicristalinas
    vertices = []
    # Vértices tipo (±1, ±1, 0, 0, 0, 0, 0, 0) y permutaciones
    for i in range(8):
        for j in range(i + 1, 8):
            v = np.zeros(8)
            v[i], v[j] = 1, 1
            vertices.append(v)
            vertices.append(-v)
    # Vértices tipo (±1/2, ±1/2, ±1/2, ±1/2, ±1/2, ±1/2, ±1/2, ±1/2) con número par de signos +
    for s in [(1, 1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, -1, -1, -1, -1)]:
        v = np.array(s) / 2
        vertices.append(v)
        vertices.append(-v)
    return np.array(vertices) * phi  # Escalar por proporción áurea para simetría

def project_to_4d(vertices):
    """Proyecta vértices de 8D a 4D usando una matriz de proyección."""
    # Matriz de proyección 8D -> 4D (aleatoria simplificada, idealmente ortogonal)
    projection_matrix = np.random.randn(4, 8)
    projection_matrix /= np.linalg.norm(projection_matrix, axis=1)[:, None]  # Normalizar
    return np.dot(vertices, projection_matrix.T)

def project_to_3d(vertices_4d, window_size=1.0):
    """Proyecta de 4D a 3D usando una ventana de corte para un cuasicristal."""
    # Matriz de proyección 4D -> 3D
    projection_matrix = np.random.randn(3, 4)
    projection_matrix /= np.linalg.norm(projection_matrix, axis=1)[:, None]
    projected = np.dot(vertices_4d, projection_matrix.T)
    
    # Ventana de corte: seleccionar puntos dentro de un cubo en el espacio ortogonal
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

# Configuración de la figura
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Generar y proyectar vértices del E8
e8_vertices = generate_e8_vertices()
vertices_4d = project_to_4d(e8_vertices)
points_3d = project_to_3d(vertices_4d, window_size=2.0)

# Generar tetraedros
points, simplices = generate_tetrahedra(points_3d)

# Visualizar
plot_tetrahedra(ax, points, simplices)

# Ajustar límites
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("E8-Derived Quasicrystal Projection (3D)")

# Texto explicativo sobre QSN y E8 (adaptado de tu código)
text = (
    "The Quasicrystalline Spin Network (QSN) and E8\n\n"
    "The QSN is a 3D quasicrystalline point space derived from the E8 lattice, "
    "an 8D structure representing the densest sphere packing. The E8's Gosset polytope "
    "(240 vertices) may encode all particles and forces in our universe via gauge symmetry transformations.\n\n"
    "This visualization shows a 3D projection of an E8-derived quasicrystal, forming tetrahedra. "
    "The QSN models physics as tetrahedra at Planck scale, changing states at 10^44 frames per second, "
    "potentially giving rise to particles and physical laws.\n\n"
    "The QSN is a subspace of the Elser-Sloane 4D quasicrystal, itself a projection of E8. "
    "This '5D printer' concept envisions the QSN generating universes by projecting E8 patterns."
)
ax.text(2.5, 2.5, 2.5, text, fontsize=8, bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))

plt.show()
