#include <GL/glut.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define num_tetrahedra 500
#define phi ((1 + sqrt(5)) / 2)

// Variables para la posición de la cámara
float cameraX = 5.0, cameraY = 5.0, cameraZ = 5.0;

typedef struct {
    float x, y, z;
} Point3D;

Point3D generate_rotation() {
    Point3D rotation;
    rotation.x = (float)rand() / RAND_MAX * 2 * M_PI;
    rotation.y = (float)rand() / RAND_MAX * 2 * M_PI;
    rotation.z = (float)rand() / RAND_MAX * 2 * M_PI;
    return rotation;
}

Point3D generate_offset() {
    Point3D offset;
    offset.x = (float)rand() / RAND_MAX * 10 - 5;
    offset.y = (float)rand() / RAND_MAX * 10 - 5;
    offset.z = (float)rand() / RAND_MAX * 10 - 5;
    return offset;
}

void generate_quasicrystal_tetrahedron(Point3D *vertices, float size) {
    Point3D rotation = generate_rotation();
    Point3D offset = generate_offset();

    vertices[0].x = 0;
    vertices[0].y = 0;
    vertices[0].z = 0;

    vertices[1].x = size;
    vertices[1].y = 0;
    vertices[1].z = 0;

    vertices[2].x = phi * size;
    vertices[2].y = phi * size;
    vertices[2].z = 0;

    vertices[3].x = phi * size;
    vertices[3].y = 0;
    vertices[3].z = phi * size;

    // Apply rotation
    for (int i = 0; i < 4; i++) {
        float x = vertices[i].x;
        float y = vertices[i].y;
        float z = vertices[i].z;
        vertices[i].x = cos(rotation.x) * cos(rotation.y) * x +
                        cos(rotation.x) * sin(rotation.y) * sin(rotation.z) * y +
                        sin(rotation.x) * cos(rotation.z) * z;
        vertices[i].y = -sin(rotation.x) * cos(rotation.y) * x -
                        sin(rotation.x) * sin(rotation.y) * sin(rotation.z) * y +
                        cos(rotation.x) * cos(rotation.z) * z;
        vertices[i].z = -sin(rotation.y) * x +
                        cos(rotation.y) * sin(rotation.z) * y +
                        cos(rotation.y) * cos(rotation.z) * z;
    }

    // Apply offset
    for (int i = 0; i < 4; i++) {
        vertices[i].x += offset.x;
        vertices[i].y += offset.y;
        vertices[i].z += offset.z;
    }
}

void draw_tetrahedron(Point3D *vertices) {
    glBegin(GL_TRIANGLES);
    // Base
    glVertex3f(vertices[0].x, vertices[0].y, vertices[0].z);
    glVertex3f(vertices[1].x, vertices[1].y, vertices[1].z);
    glVertex3f(vertices[2].x, vertices[2].y, vertices[2].z);

    // Side 1
    glVertex3f(vertices[0].x, vertices[0].y, vertices[0].z);
    glVertex3f(vertices[1].x, vertices[1].y, vertices[1].z);
    glVertex3f(vertices[3].x, vertices[3].y, vertices[3].z);

    // Side 2
    glVertex3f(vertices[0].x, vertices[0].y, vertices[0].z);
    glVertex3f(vertices[2].x, vertices[2].y, vertices[2].z);
    glVertex3f(vertices[3].x, vertices[3].y, vertices[3].z);

    // Side 3
    glVertex3f(vertices[1].x, vertices[1].y, vertices[1].z);
    glVertex3f(vertices[2].x, vertices[2].y, vertices[2].z);
    glVertex3f(vertices[3].x, vertices[3].y, vertices[3].z);
    glEnd();
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    gluLookAt(cameraX, cameraY, cameraZ, 0, 0, 0, 0, 1, 0); // Set the camera position

    glColor3f(0, 0, 1); // Blue color

    for (int i = 0; i < num_tetrahedra; i++) {
        Point3D vertices[4];
        generate_quasicrystal_tetrahedron(vertices, 1.0);
        draw_tetrahedron(vertices);
    }

    glutSwapBuffers();
}

void init() {
    glClearColor(1, 1, 1, 1); // Set background color to white
    glEnable(GL_DEPTH_TEST);
}

void specialKeys(int key, int x, int y) {
    // Modificar la posición de la cámara según la tecla presionada
    switch (key) {
        case GLUT_KEY_LEFT:
            cameraX -= 0.1;
            break;
        case GLUT_KEY_RIGHT:
            cameraX += 0.1;
            break;
        case GLUT_KEY_UP:
            cameraY += 0.1;
            break;
        case GLUT_KEY_DOWN:
            cameraY -= 0.1;
            break;
    }
    glutPostRedisplay(); // Solicitar una redibujado de la ventana
}

int main(int argc, char **argv) {
    srand(123); // Seed for reproducibility
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Quasicrystalline Spin Network (QSN)");

    glutDisplayFunc(display);
    glutSpecialFunc(specialKeys); // Registramos la función specialKeys como callback para las teclas especiales
    init();
    glutMainLoop();
    return 0;
}
