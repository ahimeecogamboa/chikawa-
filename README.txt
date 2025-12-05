Sistema de Registro de Ventas en Python
Chiikawa shop

Este proyecto consiste en desarrollar un sistema de registro de ventas que permite gestionar productos dentro de un proceso de compra. El usuario puede registrar compras de productos disponibles en la tienda, pudiendo agregar uno o más elementos a su lista, haciendo un archivo txt que incluye cantidad y precio, visualizar la lista actual de compras, calcular el precio total, con descuento (si este aplica en los parámetros establecidos de 10% de descuento a partir de 1000$ en compras) y generar unna ventana de información en especie de recibo(muestra el subtotal, descuento y el total), eliminar productos de la lista. A su vez, puede visualizar en un gráfico la estadística de las ventas realizadas y una demostración que representa los productos más vendidos.
El programa fue creado como integración de conocimientos obtenidos, utilizando los fundamentos de la programación y una solución funcional aplicada a un problema real del área comercial, volviendo el proceso de registro y cálculo de ventas más accesible y sencillo.

Para su uso en Visual Studio se requiere contar con los archivos de imágen y con las librerías necesarias instaladas correctamente, las cuales incluyen: pandas, tkinter, colorama, matplotlib, pillow, Os, random, time y playsound3.

Antes de ejecutar el programa:
Es importante guardar los archivos del programa y asegurarse que el directorio dentro del programa concuerde con el  del equipo tanto en la sección donde se ultiliza playsound (DEFmodulo, desde la línea 59-69), como en main desde la línea 22-28.

Al iniciar el programa se despliega la ventana de menú donde se muestran las siguientes opciones:
1. Registrar venta
2. Mostrar ventas
3. Calcular total de ventas
4. Mostrar gráfica de ventas
5. Eliminar una venta
6. Salir
Cada una con una función específica explicada a continuación.
1. Registrar venta: al seleccionar esta opción, se desplegará una venta que te permitirá seleccionar un producto a la vez, la acción se realizará una vez se presione el botón <Registrar>
2. Mostrar ventas: al seleccionar esta opción se nos mostrará una lista donde se indica el nombre del producto, la cantidad, el precio unitario y el total por cada modelo.
3. Calcular total de ventas: está acción nos mostrará una ventana emergente que nos presenta el subtotal (incluyendo todos los productos agregados), el descuento aplicado (a partir de 1000$ se aplica un 10%), y el total tras restar el descuento en caso de contar con él.
4. Mostrar gráfica de ventas: tras presionar dicho botón, se nos mostrará una gráfica de pastel que nos indique el porcentaje de ventas de los modelos entre el total de ventas.
5. Eliminar venta: nos dará la oportunidad de eliminar un producto de nuestra lista. La acción solo se realizará una vez se seleccione el producto a retirar y se presione el botón <Eliminar>
6. Salir: termina el ciclo y cierra el programa.

Por ejemplo, si busco comprar tres veces el mismo modelo de peluche, primero inicio el programa, después selecciono la opción de registrar venta y busco el modelo que deseo, y repito dicha acción las tres veces que son necesarias. Después para comprobar que se registraron correctamente selecciono la opción de mostrar ventas, esto me dará  la lista de los productos ya registrados y un vistazo de el precio total a pagar por modelo de peluche. Como siguiente paso, selecciono la opción de calcular total de ventas, notaremos que en este caso no aplica el descuento, así que solo se nos mostrará el total directamente.
Al finalizar, notas que agregaste un producto de más, así que deseas eliminarlo, lo siguiente es la opción de eliminar venta, seleccionas el producto a eliminar y quedaría todo listo. Todos estos procesos que podrían tomar más tiempo de otra manera, aquí logras analizar en un momento tu total e incluso si aplicas para descuentos.
Lo único que falta es salir.