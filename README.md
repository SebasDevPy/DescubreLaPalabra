
# parcial°2 de programacion

### 👥integrantes: 
- Justin Prado
- Carlos Lopez
- Sebastian Castiñeiras
  
## 🎮**JUEGO**:

[![titulo-inicio.png](https://i.postimg.cc/1XHqYc62/titulo-inicio.png)](https://postimg.cc/K31j1T0D)

### Sobre el juego: 

El juego comienza con una pantalla de inicio que, principalmente, pedirá tu nombre para poder guardar tu desempeño mediante tu score, que se registrará junto con tu nombre o nickname. No se permitirán espacios, y si esto ocurre, el juego te dará una advertencia.




[![pantalla-de-inicio.png](https://i.postimg.cc/CxJcfkQv/pantalla-de-inicio.png)](https://postimg.cc/tsZ3KZyP)

Después de pedirle al usuario su nickname, comenzará la "Pantalla de Juego". Aquí es donde se desarrollará toda la funcionalidad del juego. En esta pantalla se mostrará una palabra de 6 letras, la cual estará desordenada visualmente para el jugador. Estas letras estarán dibujadas como burbujas.

Debajo de las burbujas, habrá un rectángulo que mostrará la puntuación (score) según las combinaciones acertadas, un temporizador que indicará el tiempo límite para acertar, un botón "Submit" para ingresar la combinación que el usuario haya formado, un botón "Shuffle" para alterar el orden de las letras aleatoriamente, y un botón "Clear" para borrar las letras que el jugador haya formado.

Por último, debajo de este rectángulo se mostrarán todas las palabras acertadas que el jugador haya formado. La partida finalizará cuando se acabe el tiempo o cuando ya no haya más palabras que formar.



[![pantalla-del-juego.png](https://i.postimg.cc/mZ8kJrJv/pantalla-del-juego.png)](https://postimg.cc/s1G3Z3Vm)

Si el tiempo llega a 0, aparecerá una pequeña ventana que te dará dos opciones: "Sí" y "No". Dependiendo de tu elección, continuarás jugando hasta completar tres partidas o terminarás tu partida, guardando tu score.

[![pantalla-continuar.png](https://i.postimg.cc/fbcTKWYg/pantalla-continuar.png)](https://postimg.cc/QBM3N34p)




Lo siguiente será la pantalla final, la parte que finalizará el juego. En esta pantalla se mostrará el top 5 de los mayores scores guardados en el juego junto con su respectivo nickname. Habrá un botón Close que cerrará el programa y con esto finalizará el juego.



[![6.png](https://i.postimg.cc/jdVT8whq/6.png)](https://postimg.cc/9zBs0fSs)



## LOGICA DE JUEGO:

### Pantalla inicio:
Comenzamos con la clase Inicio que inicializará atributos para:
- inicilizamos pygame.
- Cargar imágenes.
- Regular la escala de estas imágenes.
- Crear rectángulos para gestionar colisiones y posicionamiento.
- Configurar fuentes para renderizar textos en esta pantalla.
- creo algunas banderas que se utlizaran en los metodos de la clase.
- un rectangulo**input box** que este sera donde el usuario podra escribir su name
Estos atributos asegurarán que todos los elementos gráficos y de lógica estén preparados para la pantalla de inicio del juego.


[![iniciar.png](https://i.postimg.cc/Kc0cJvHR/iniciar.png)](https://postimg.cc/PN8kqhhj)



- Seguiremos con el bucle de esta pantalla, que pertenecerá a un método de la clase Inicio. El while será la principal funcionalidad. Tomaremos los eventos, que serán las distintas acciones que hará la persona, y Pygame las interpretará como presionar teclas, mover el mouse, hacer clics, etc. Esto lo haremos con un for, iterando sobre los distintos eventos.

- Un evento importante para esta parte es el backspace. Este se utiliza cuando queremos verificar si la persona desea borrar lo que está escribiendo en el rect (input). Mediante un slice, se ignorará el último elemento cuando se presione la tecla.

- La forma en la que se validará que las letras que el usuario introduce en el input no se salgan del rango del rect del input será mediante un if que validará la longitud del texto ingresado con el método **get_width()**. Si esta longitud es mayor que la longitud del rect del input, se hará un slice que eliminará una letra del texto ingresado y se renderizará el nuevo texto ingresado.





[![2.png](https://i.postimg.cc/7hRkDhF9/2.png)](https://postimg.cc/0K730k2K)





- actualizaremos constantemente el fondo de pantalla
- bliearemos los distintitos rects, botones, textos,avisos
-  mediante una funcion llamada **validar_espacioes** que si encuentra mas de un espacio(**" "**) en en el texto ingresado si pasa esta validacion se hara aviso al usario mediante un texto que se bliteara una determinda cordenada dentro del cuadro donde esta el rect y eliminaremos el texto ingresado,


[![3.png](https://i.postimg.cc/sDtrNB9D/3.png)](https://postimg.cc/7fMdCZWp)


### clase_juego
En este archivo se desenvuelve el funcionamiento principal del juego, dando a su funcionamiento el proceso principal del mismo. Aqui encontraremos funciones que desordenan palabras, las compara con lo ingresado por el usuario y valida que sean correctas para sumar puntos (1 punto por cada caracter de la palabra formada); se controla el tiempo de duración de cada partida y el posicionamiento de las imagenes del juego.


[![clase-juego.png](https://i.postimg.cc/CL8114zg/clase-juego.png)](https://postimg.cc/F79mC3yW)

### clase_continuar:

En este archivo funciona una ventana emergente la cual avisa al usuario que puede o no continuar jugando tras la finalizacion de su 1er partida (dando un maximo de 3 oportunidades).



[![class-continuar.png](https://i.postimg.cc/rF2jZMR2/class-continuar.png)](https://postimg.cc/z3pTVmkx)




### clase_final:

Este archivo tiene la funcionalidad de mostrar en una nueva ventana la puntuacion de los mejores jugadores que han participado en el videojuego.

[![Captura-de-pantalla-2024-07-01-132910.png](https://i.postimg.cc/4xsggDMr/Captura-de-pantalla-2024-07-01-132910.png)](https://postimg.cc/2VcJdKCw)

### Package_funciones:

En este paquete almacenamos validaciones correspondientes al programa, proceso de carga de usuarios y almacenamiento en archivo csv y json para los usuarios creados con su id unica y puntuaciones (en csv) y para json el "nickname" del usuario con su puntuacion.



[![csv.png](https://i.postimg.cc/V67RJ8Zd/csv.png)](https://postimg.cc/FdLc6244)



cargar jugador



[![cargarjugador.png](https://i.postimg.cc/JhpYSvVc/cargarjugador.png)](https://postimg.cc/67GhvHQy)







## BASADO EN:

LINK:
https://www.1001juegos.com/juego/pop-a-word?utm_source=invite&roomId=7jk43po5


