# escaner_puertos.py

Este script de Python crea un escáner de puertos básico con las siguientes características:

1. Solicita al usuario que ingrese la dirección IP objetivo.
2. Escanea los primeros 1024 puertos (puertos bien conocidos).
3. Utiliza hilos (threads) para realizar el escaneo de manera más rápida.
4. Muestra los puertos abiertos a medida que los encuentra.
5. Al finalizar, muestra una lista de todos los puertos abiertos encontrados.


Para usar este escáner:

1. Guarda el código en un archivo llamado `escaner_puertos.py`.
2. Abre una terminal o línea de comandos.
3. Navega hasta el directorio donde guardaste el archivo.
4. Ejecuta el script con el comando: `python escaner_puertos.py`
5. Ingresa la dirección IP que deseas escanear cuando se te solicite.


Advertencias importantes:

1. Usa este script solo en redes y sistemas para los que tengas permiso explícito.
2. El escaneo de puertos sin autorización puede ser ilegal en algunos contextos.
3. Algunos firewalls o sistemas de seguridad pueden detectar y bloquear este tipo de escaneo.


Este es un escáner potente pero basico y puede no detectar todos los puertos abiertos en sistemas más complejos o protegidos. Para un uso profesional, considera herramientas más avanzadas como Nmap.

Para usar el código de manera segura y educativa:

1. Configura una máquina virtual o un entorno de laboratorio controlado.
2. Practica el escaneo en tus propios dispositivos o en sistemas de prueba.
3. Estudia cómo diferentes configuraciones de firewall y seguridad afectan los resultados del escaneo.


Recuerda, la ciberseguridad trata tanto de proteger sistemas como de entender cómo podrían ser vulnerables. Usa este conocimiento de manera responsable y siempre dentro de los límites éticos y legales.

Este código mejorado incluye las siguientes características:

1. Verificación de conectividad: Realiza un ping antes de iniciar el escaneo para verificar si el host está accesible.
2. Opciones de rango de puertos: Permite al usuario elegir entre escanear puertos bien conocidos, todos los puertos, o un rango personalizado.
3. Tiempo de espera aumentado: El `timeout` para las conexiones se ha incrementado a 2 segundos para dar más tiempo a las respuestas.
4. Mejor manejo de resultados: Proporciona un mensaje más informativo si no se encuentran puertos abiertos.
5. Flexibilidad: Permite continuar con el escaneo incluso si el ping falla, dando al usuario la opción de proceder.


Para usar este escáner mejorado:

1. Guarda el código en un archivo llamado `escaner_puertos.py`.
2. Abre una terminal o línea de comandos.
3. Navega hasta el directorio donde guardaste el archivo.
4. Ejecuta el script con el comando: `python escaner_puertos.py`
5. Sigue las instrucciones en pantalla para ingresar la dirección IP y seleccionar el rango de puertos.


Recuerda este escáner es potente, por lo que es aún más importante usarlo de manera ética y responsable. Úsalo solo en sistemas y redes para los que tengas permiso explícito.
