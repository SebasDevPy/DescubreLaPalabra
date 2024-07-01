
# parcial°2 de programacion

### 👥integrantes: 
- Justin Prado
- Carlos Lopez
- Sebastian Castiñeiras
  
## 🎮**JUEGO**:

![titulo_inicio](https://github.com/Rias05/ejemplo.makdown/assets/119630600/08185309-33d2-4823-aebd-eafa88d1760b)

### Sobre el juego: 

El juego comienza con una pantalla de inicio que, principalmente, pedirá tu nombre para poder guardar tu desempeño mediante tu score, que se registrará junto con tu nombre o nickname. No se permitirán espacios, y si esto ocurre, el juego te dará una advertencia.
[pantalla-de-inicio.png](https://postimg.cc/tsZ3KZyP)



Después de pedirle al usuario su nickname, comenzará la "**Pantalla de Juego**". Aquí es donde se desarrollará toda la funcionalidad del juego. En esta pantalla se mostrará una palabra de 6 letras, la cual estará desordenada visualmente para el jugador. Estas letras estarán dibujadas como burbujas.

Debajo de las burbujas, habrá un rectángulo que mostrará la puntuación (score) según las combinaciones acertadas, un temporizador que indicará el tiempo límite para acertar, un botón "**Submit**" para ingresar la combinación que el usuario haya formado, un botón "**Shuffle**" para alterar el orden de las letras aleatoriamente y un botón "**Clear**" para borrar las letras que el jugador haya formado.

Por último, debajo de este rectángulo se mostrarán todas las palabras acertadas que el jugador haya formado. La partida finalizará cuando se acabe el tiempo o cuando ya no haya más palabras que formar.





<img width="700" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/ea42a445-c248-44eb-8bec-95206aab8c98">


Si el tiempo llega a 0, aparecerá una pequeña ventana que te dará dos opciones: "Sí" y "No". Dependiendo de tu elección, continuarás jugando hasta completar tres partidas o terminarás tu partida, guardando tu score.


<img width="500" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/050a9f50-afae-4955-b175-1cc3c91a23f2">

Al haber presionado "No" o "Si" tus partidas llegaron al límite de 3, se mostrará una pantalla en un pequeño lapso de tiempo que indicará tu puntaje durante tus partidas.
<img width="840" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/4ab8e6ab-0718-474e-af49-1f16650a645e">




Lo siguiente será la pantalla final, la parte que finalizará el juego. En esta pantalla se mostrará el top 5 de los mayores scores guardados en el juego junto con su respectivo nickname. Habrá un botón Close que cerrará el programa y con esto finalizará el juego.

<img width="700" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/79679234-23b2-4f14-b026-a0c6a4d8b782">




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

<img width="553" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/4a6a64c3-fdfc-4a98-bd5e-798219132e05">


- Seguiremos con el bucle de esta pantalla, que pertenecerá a un método de la clase Inicio. El while será la principal funcionalidad. Tomaremos los eventos, que serán las distintas acciones que hará la persona, y Pygame las interpretará como presionar teclas, mover el mouse, hacer clics, etc. Esto lo haremos con un for, iterando sobre los distintos eventos.

- Un evento importante para esta parte es el backspace. Este se utiliza cuando queremos verificar si la persona desea borrar lo que está escribiendo en el rect (input). Mediante un slice, se ignorará el último elemento cuando se presione la tecla.

- La forma en la que se validará que las letras que el usuario introduce en el input no se salgan del rango del rect del input será mediante un if que validará la longitud del texto ingresado con el método **get_width()**. Si esta longitud es mayor que la longitud del rect del input, se hará un slice que eliminará una letra del texto ingresado y se renderizará el nuevo texto ingresado.






<img width="700" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/28b4f944-b566-48bc-86a2-5d080a4d3da6">


- actualizaremos constantemente el fondo de pantalla
- bliearemos los distintitos rects, botones, textos,avisos
-  mediante uan funcion llamada **validar_espacioes** que si encuentra mas de un espacio(**" "**) en en el texto ingresado si pasa esta validacion se hara aviso al usario mediante un texto que se bliteara una determinda cordenada dentro del cuadro donde esta el rect y eliminaremos el texto ingresado,


<img width="599" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/865b9b66-5cf3-49d9-9c9e-89a8f3825216">

### clase_juego
En este archivo se desenvuelve el funcionamiento principal del juego, dando a su funcionamiento el proceso principal del mismo. Aqui encontraremos funciones que desordenan palabras, las compara con lo ingresado por el usuario y valida que sean correctas para sumar puntos (1 punto por cada caracter de la palabra formada); se controla el tiempo de duración de cada partida y el posicionamiento de las imagenes del juego.

<img width="539" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/e708c7b8-1686-40f8-9ffd-1bd65f2a90fb">

### clase_continuar:

En este archivo funciona una ventana emergente la cual avisa al usuario que puede o no continuar jugando tras la finalizacion de su 1er partida (dando un maximo de 3 oportunidades).

<img width="674" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/80b41aa3-99c2-442c-9db1-c6b60c90a792">


### clase_final:

Este archivo tiene la funcionalidad de mostrar en una nueva ventana la puntuacion de los mejores jugadores que han participado en el videojuego.

<img width="503" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/a3a093a1-8cbe-4202-964d-f19c9f1b6c49">


### Package_funciones:

En este paquete almacenamos validaciones correspondientes al programa, proceso de carga de usuarios y almacenamiento en archivo csv y json para los usuarios creados con su id unica y puntuaciones (en csv) y para json el "nickname" del usuario con su puntuacion.

<img width="500" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/a7157d73-374d-4ebf-91a2-72fc49fe9641">


<img width="533" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/1365c58f-a993-481a-acde-3b8dd2c561fe">


<img width="500" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/d657e7c0-0971-40dc-8cdc-ee69f2a7fc62">


<img width="600" alt="image" src="https://github.com/Rias05/ejemplo.makdown/assets/119630600/3cfc6fe3-dbb7-4e52-a248-f06b8886debe">

## BASADO EN:

LINK:
https://www.1001juegos.com/juego/pop-a-word?utm_source=invite&roomId=7jk43po5


