# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `create_correlation_circuit` | function | `life.py:68` | `def create_correlation_circuit(num_qubits, interactions)` |
| `generate_e8_vertices` | function | `life.py:9` | `def generate_e8_vertices(num_vertices)` |
| `generate_hexagonal_grid` | function | `life.py:33` | `def generate_hexagonal_grid(radius, num_rings)` |
| `generate_tetrahedra` | function | `life.py:45` | `def generate_tetrahedra(points)` |
| `plot_flower_of_life` | function | `life.py:62` | `def plot_flower_of_life(ax2d, centers, radius)` |
| `plot_tetrahedra` | function | `life.py:54` | `def plot_tetrahedra(ax, points, simplices, color)` |
| `project_to_3d` | function | `life.py:25` | `def project_to_3d(vertices, window_size)` |
| `Point3D` | struct | `main.c:12` | `` |
| `display` | function | `main.c:99` | `void display()` |
| `draw_tetrahedron` | function | `main.c:75` | `void draw_tetrahedron(Point3D *vertices)` |
| `generate_offset` | function | `main.c:23` | `Point3D generate_offset()` |
| `generate_quasicrystal_tetrahedron` | function | `main.c:31` | `void generate_quasicrystal_tetrahedron(Point3D *vertices, float size)` |
| `generate_rotation` | function | `main.c:15` | `Point3D generate_rotation()` |
| `glBegin` | function | `main.c:77` | `glBegin(GL_TRIANGLES);` |
| `glClear` | function | `main.c:101` | `glClear(GL_COLOR_BUFFER_BIT \| GL_DEPTH_BUFFER_BIT);` |
| `glClearColor` | function | `main.c:117` | `glClearColor(1, 1, 1, 1);` |
| `glColor3f` | function | `main.c:104` | `glColor3f(0, 0, 1);` |
| `glEnable` | function | `main.c:118` | `glEnable(GL_DEPTH_TEST);` |
| `glEnd` | function | `main.c:97` | `glEnd();` |
| `glLoadIdentity` | function | `main.c:102` | `glLoadIdentity();` |
| `glVertex3f` | function | `main.c:79` | `glVertex3f(vertices[0].x, vertices[0].y, vertices[0].z);` |
| `gluLookAt` | function | `main.c:103` | `gluLookAt(cameraX, cameraY, cameraZ, 0, 0, 0, 0, 1, 0);` |
| `glutCreateWindow` | function | `main.c:145` | `glutCreateWindow("Quasicrystalline Spin Network (QSN)");` |
| `glutDisplayFunc` | function | `main.c:146` | `glutDisplayFunc(display);` |
| `glutInit` | function | `main.c:142` | `glutInit(&argc, argv);` |
| `glutInitDisplayMode` | function | `main.c:143` | `glutInitDisplayMode(GLUT_DOUBLE \| GLUT_RGB \| GLUT_DEPTH);` |
| `glutInitWindowSize` | function | `main.c:144` | `glutInitWindowSize(800, 600);` |
| `glutMainLoop` | function | `main.c:150` | `glutMainLoop();` |
| `glutPostRedisplay` | function | `main.c:137` | `glutPostRedisplay();` |
| `glutSpecialFunc` | function | `main.c:148` | `glutSpecialFunc(specialKeys);` |
| `glutSwapBuffers` | function | `main.c:112` | `glutSwapBuffers();` |
| `init` | function | `main.c:115` | `void init()` |
| `main` | function | `main.c:139` | `int main(int argc, char **argv)` |
| `num_tetrahedra` | macro | `main.c:5` | `#define num_tetrahedra` |
| `phi` | macro | `main.c:7` | `#define phi` |
| `specialKeys` | function | `main.c:120` | `void specialKeys(int key, int x, int y)` |
| `srand` | function | `main.c:141` | `srand(123);` |
| `generate_quasicrystal_tetrahedron` | function | `main.py:6` | `def generate_quasicrystal_tetrahedron(size)` |
| `plot_tetrahedron` | function | `main.py:29` | `def plot_tetrahedron(ax, vertices, color)` |
| `generate_e8_vertices` | function | `someideas.py:6` | `def generate_e8_vertices()` |
| `generate_tetrahedra` | function | `someideas.py:43` | `def generate_tetrahedra(points)` |
| `plot_tetrahedra` | function | `someideas.py:52` | `def plot_tetrahedra(ax, points, simplices, color)` |
| `project_to_3d` | function | `someideas.py:32` | `def project_to_3d(vertices_4d, window_size)` |
| `project_to_4d` | function | `someideas.py:25` | `def project_to_4d(vertices)` |
| `create_ising_circuit` | function | `someideas2.py:54` | `def create_ising_circuit(num_qubits, interactions)` |
| `generate_e8_vertices` | function | `someideas2.py:9` | `def generate_e8_vertices(num_vertices)` |
| `generate_tetrahedra` | function | `someideas2.py:37` | `def generate_tetrahedra(points)` |
| `plot_tetrahedra` | function | `someideas2.py:46` | `def plot_tetrahedra(ax, points, simplices, color)` |
| `project_to_3d` | function | `someideas2.py:27` | `def project_to_3d(vertices, window_size)` |
| `generate_quasicrystal_tetrahedron` | function | `transmision_qbits.py:54` | `def generate_quasicrystal_tetrahedron(size)` |
| `plot_tetrahedron` | function | `transmision_qbits.py:77` | `def plot_tetrahedron(ax, vertices, color)` |
| `simulate_qubit_transmission` | function | `transmision_qbits.py:6` | `def simulate_qubit_transmission(qubit_state, measurement_basis, num_samples)` |
