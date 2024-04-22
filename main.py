import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.spatial import Delaunay

def generate_quasicrystal_tetrahedron(size=1.0):
    phi = (1 + np.sqrt(5)) / 2  # Razón áurea
    vertices = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [phi, phi, 0],
        [phi, 0, phi]
    ])

    rotation = np.random.uniform(0, 2 * np.pi, 3)
    rotated_vertices = np.zeros_like(vertices)
    for i in range(4):
        rotated_vertices[i] = size * (
            np.cos(rotation[0]) * np.cos(rotation[1]) * vertices[i] +
            np.cos(rotation[0]) * np.sin(rotation[1]) * np.sin(rotation[2]) * vertices[i] +
            np.sin(rotation[0]) * np.cos(rotation[2]) * vertices[i]
        )

    offset = np.random.uniform(-5, 5, 3)
    rotated_vertices += offset

    return rotated_vertices

def plot_tetrahedron(ax, vertices, color='b'):
    try:
        faces = Delaunay(vertices).simplices
        for face in faces:
            x = vertices[face, 0]
            y = vertices[face, 1]
            z = vertices[face, 2]
            ax.plot_trisurf(x, y, z, color=color, alpha=0.5)
    except RuntimeError as e:
        print("Error al graficar un tetraedro:", e)

# Configuración de la figura y el eje
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Generación y visualización de los tetraedros
num_tetrahedra = 500
for _ in range(num_tetrahedra):
    tetrahedron_vertices = generate_quasicrystal_tetrahedron()
    plot_tetrahedron(ax, tetrahedron_vertices, color='b')

# Ajustar los límites y el aspecto visual del gráfico
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título y leyenda
plt.title("Quasicrystalline Spin Network (QSN)")
plt.legend(['Tetrahedra'], loc='upper right')
# Descripción detallada de la relación entre el QSN y E8
text = ("The QSN and Its Mapping to E8\n\n"
        "The Quasicrystalline Spin Network (QSN) is a 3D quasicrystalline point space on which we model physics. "
        "The QSN is deeply related to the E8 crystal. "
        "The following is a brief explanation of the relationship between the various related objects.\n\n"
        "CQC-QSN-mapping to upload20G-LR-L-R\n\n"
        "We begin with an 8-dimensional crystal called the E8 lattice. The E8 lattice is an 8D point set "
        "representing the densest packing of spheres in 8D. The basic cell of the E8 lattice, the Gosset polytope, "
        "has 240 vertices and accurately corresponds to all particles and forces in our (3D) reality and their "
        "interactions, specifically the way they can all transform from one to another through a process called "
        "gauge symmetry transformation.\n\n"
        "The QSN is composed of tetrahedra that form many different vertex types. The above mentioned 20-Group "
        "is one of them. Here are examples of other vertex types:\n\n"
        "QSN-Vertex-Types-Samples\n\n"
        "This is the QSN:\n\n"
        "CQC-QSN-mapping to upload\n\n"
        "And now to the connection between the QSN, which started its life as the point space representing the most "
        "efficient sphere packing in 3D, and the 4D-quasicrystal-derived Compound Quasicrystal, which started its life "
        "as E8, the most efficient sphere packing in 8D: as it turns out, the Compound Quasicrystal is an exact subspace "
        "of the QSN. The QSN contains all legal configurations of the Elser-Sloane, 8D-to-4D quasicrystal.\n\n"
        "The QSN is therefore deeply related to the E8 lattice and its 4D projection.\n\n"
        "In simplistic terms, you can think of the QSN as a 3D version of a 2D TV screen. A 2D TV screen is made up of "
        "2D pixels that change brightness and color levels from one video frame to the next at a certain speed (for example "
        "24 frames per second in most modern movies).\n\n"
        "Now we can use our QSN geometry as a toy model for physics!\n\n"
        "Similarly, the QSN is a 3D grid of Planck scale, tetrahedron-shaped “pixels” that, via the rules of a binary, "
        "geometric language/code, exist at each “frame” of reality as either on or off, and if on, then rotated left or right. "
        "These pixels populate the QSN, and their states change from one frame to the next, at a “universal frame rate” of "
        "10^44 frames per second (the “Planck time”). Over many of these frames patterns emerge on this 3D quasicrystal. "
        "These patterns become more and more meaningful and sophisticated with time. After a while, particles begin to form "
        "on the quasicrystal. With time, these particles take on more and more complex forms, and eventually the reality we "
        "all know, love and play video games in, emerges.")
ax.text(11, 9, 15, text, fontsize=8, bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))

# Mostrar el gráfico
plt.show()
