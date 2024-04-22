# The-QSN-and-Its-Mapping-to-E8
The QSN and Its Mapping to E8

![CQC-QSN-mapping-to-upload-287x300](https://github.com/grisuno/The-QSN-and-Its-Mapping-to-E8/assets/1097185/5b4f5d2c-dcf4-49e1-8b4f-dcdca7dd35e0)

## Descripción
Este proyecto visualiza la red de hilos cuasicristalinos (QSN) y su relación con la red cristalina E8 en un entorno tridimensional. Se generan y visualizan tetraedros en una cuadrícula quasicristalina utilizando Python y la biblioteca Matplotlib.

![20G-LR-L-R-300x295](https://github.com/grisuno/The-QSN-and-Its-Mapping-to-E8/assets/1097185/4114e072-f8f4-471e-9df1-f1048ab87cbf)

La Red de Espín Cuasicristalina (QSN, por sus siglas en inglés) y su Mapeo a E8 es un espacio de puntos cuasicristalino en 3D en el cual modelamos la física. La QSN está profundamente relacionada con el cristal E8. A continuación, se presenta una breve explicación de la relación entre los diversos objetos relacionados.

Comenzamos con un cristal de ocho dimensiones llamado retícula E8. La retícula E8 es un conjunto de puntos en 8D que representa el empaquetamiento más denso de esferas en 8D. La celda básica de la retícula E8, el politopo de Gosset, tiene 240 vértices y corresponde con precisión a todas las partículas y fuerzas en nuestra realidad tridimensional y sus interacciones, específicamente la manera en que todas pueden transformarse de una a otra a través de un proceso llamado transformación de simetría de calibre.

La primera operación que realizamos es tomar la retícula E8 y proyectar una porción de ella a 4D, a través de uno de dos procesos: corte y proyección, o mapeo de Hopf. Cualquiera de estos procesos nos da el mismo resultado: un cuasicristal de cuatro dimensiones llamado cuasicristal de Elser-Sloane. Cuando la celda básica de E8, el politopo de Gosset, se proyecta a 4D, crea dos formas idénticas de 4D de diferentes tamaños. La proporción de sus tamaños es la proporción áurea. Cada una de estas formas está construida por 600 tetraedros tridimensionales rotados entre sí por un ángulo basado en la proporción áurea. Nos referimos a esta forma de 4D como la "Célula 600". Las Células 600 interactúan de maneras específicas (se intersectan en 7 maneras relacionadas con la proporción áurea y se "besan" de una manera particular) para formar el cuasicristal de 4D.
![2-600-cells-smaller-1024x554](https://github.com/grisuno/The-QSN-and-Its-Mapping-to-E8/assets/1097185/da51454a-cb75-4843-99ad-b3a276488b09)
![2-600-cells-smaller-1024x554](https://github.com/grisuno/The-QSN-and-Its-Mapping-to-E8/assets/1097185/ab196220-62d3-4c61-b943-cdce05797f3e)

A continuación, tomamos cinco subespacios tridimensionales de este cuasicristal de 4D (un subespacio siendo todos los tetraedros orientados en la misma dirección) y los rotamos entre sí por 15.522 grados, obtenemos un cuasicristal tridimensional que puede ser visto como una representación del cuasicristal de 4D, Elser-Sloane. Llamamos a esto el "Cuasicristal Compuesto" (CQC). Aquí hay una representación de cinco subespacios: la imagen en la izquierda es un subespacio, la segunda tiene un segundo subespacio superpuesto y así sucesivamente. La quinta imagen es el CQC.

¿Por qué es importante el Cuasicristal Compuesto? Es importante por su relación con la QSN. La QSN (Red de Espín Cuasicristalino) es la red tridimensional de intercambio de puntos más densa posible (bajo ciertas restricciones) y es el espacio de puntos más eficiente computacionalmente en 3D. Cuando hablamos sobre la cadena de Fibonacci tridimensional más densa, nos referimos a cadenas de dos letras en lugar de cadenas infinitamente infladas, que es una propiedad de la QSN como cuasicristal. La QSN se crea tomando la retícula FCC (un espacio de puntos que proporciona el empaquetamiento más denso de esferas tridimensionales) y luego extendiendo sus puntos hasta que estén espaciados de acuerdo con la secuencia de Fibonacci. Poblamos este nuevo espacio de puntos extendido con tetraedros que apuntan hacia arriba y hacia abajo.

Llamemos "subespacio 1" a los tetraedros que apuntan hacia arriba y "subespacio 2" a los tetraedros que apuntan hacia abajo. Tomamos una nueva retícula de puntos espaciados por Fibonacci, la clonamos cinco veces y, como hicimos con los subespacios que formaron el Cuasicristal Compuesto, rotamos los cinco clones entre sí por 15.522 grados para crear un nuevo cuasicristal. Luego repetimos el proceso con el subespacio 2. Los subespacios 1 y 2 se combinan para crear la QSN. En esta secuencia de imágenes vemos 5 clones de 4 tetraedros en un subespacio, cada clon en un color diferente, rotándose entre sí. Los 4 tetraedros comparten un vértice, y el objeto creado a partir de las 5 rotaciones de ellos se llama Grupo 20.
![CQC-subspaces-redone-1024x216](https://github.com/grisuno/The-QSN-and-Its-Mapping-to-E8/assets/1097185/5a2572ac-e221-4d8e-891e-ddb775bd01de)

La QSN está compuesta por tetraedros que forman muchos tipos de vértices diferentes. El Grupo 20 mencionado anteriormente es uno de ellos. Aquí hay ejemplos de otros tipos de vértices.
![updown-alpha-300x284](https://github.com/grisuno/The-QSN-and-Its-Mapping-to-E8/assets/1097185/bc57846a-2a9c-4c15-a5a3-7a2602ed3f97)
![QSN-Vertex-Types-Samples-3-e1467927748157-1024x999](https://github.com/grisuno/The-QSN-and-Its-Mapping-to-E8/assets/1097185/694a9c07-2afa-4d09-9f30-2bda245fa36f)

Esta es la QSN.
![CQC-QSN-mapping-to-upload-980x1024](https://github.com/grisuno/The-QSN-and-Its-Mapping-to-E8/assets/1097185/d1374afb-bc01-4171-b708-fb0625f2d23d)

Y ahora, sobre la conexión entre la QSN, que comenzó su vida como el espacio de puntos que representa el empaquetamiento de esferas más eficiente en 3D, y el Cuasicristal Compuesto derivado de cuasicristal de 4D, que comenzó su vida como E8, el empaquetamiento de esferas más eficiente en 8D: resulta que el Cuasicristal Compuesto es un subespacio exacto de la QSN. La QSN contiene todas las configuraciones legales del cuasicristal de Elser-Sloane, de 8D a 4D.

La QSN está profundamente relacionada con la retícula E8 y su proyección de 4D.

En términos simplificados, puedes pensar en la QSN como una versión tridimensional de una pantalla de TV 2D. Una pantalla de TV 2D está compuesta por píxeles 2D que cambian de brillo y niveles de color de un fotograma de video al siguiente a una cierta velocidad (por ejemplo, 24 fotogramas por segundo en la mayoría de las películas modernas).

¡Ahora podemos usar nuestra geometría QSN como un modelo de juguete para la física!

De manera similar, la QSN es una cuadrícula tridimensional de "píxeles" en la escala de Planck, en forma de tetraedros, que, a través de las reglas de un lenguaje/código binario geométrico, existen en cada "fotograma" de la realidad como encendidos o apagados, y si están encendidos, entonces rotados hacia la izquierda o hacia la derecha. Estos píxeles poblan la QSN, y sus estados cambian de un fotograma a otro, a una "velocidad de fotogramas universal" de 10^44 fotogramas por segundo (el "tiempo de Planck"). A lo largo de muchos de estos fotogramas, emergen patrones en este cuasicristal tridimensional. Estos patrones se vuelven cada vez más significativos y sofisticados con el tiempo. Después de un tiempo, las partículas comienzan a formarse en el cuasicristal. Con el tiempo, estas partículas adoptan formas cada vez más complejas, y eventualmente, emerge la realidad que todos conocemos, amamos y en la que jugamos videojuegos.

## Contenido
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Instalación
Para utilizar este proyecto, sigue estos pasos:

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python instalado en tu sistema.
3. Instala las bibliotecas necesarias ejecutando los siguientes comandos en tu terminal:

```bash
pip install matplotlib numpy scipy
```
## Uso
Para ejecutar el script principal, sigue estos pasos:

```bash
python3 main.py
```
Abre una terminal.
Navega al directorio donde clonaste este repositorio.
Ejecuta el script principal con el siguiente comando:
```bash
python3 main.py
```
## Contribución
Las contribuciones son bienvenidas. Si tienes alguna idea para mejorar este proyecto, no dudes en abrir un issue o enviar un pull request.
la investigacion hecha con el paper en
![qgr-logo-1024x201](https://github.com/grisuno/The-QSN-and-Its-Mapping-to-E8/assets/1097185/7c721ffd-de98-4dd3-bfc6-9c682af679b4)

https://quantumgravityresearch.org/portfolio/a-deep-link-between-3d-and-8d/

## Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.
