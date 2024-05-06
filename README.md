Juego de Portero con Raspberry Pi Pico
Este proyecto implementa un juego de portero utilizando Raspberry Pi Pico y el lenguaje de programación Python. El juego consiste en un sistema que genera un indicador del tipo de portero 
que va a jugar en el turno y emite un sonido de victoria o derrota según la acción del jugador.

Requisitos
- Circuit Python 9.0.4 o posterior
- Raspberry Pi Pico con MicroPython instalado
- Librerías necesarias: board, digitalio, pwmio, time, random
  
Instrucciones de Uso
- Clona este repositorio en tu sistema local.
- Conecta tu Raspberry Pi Pico al sistema y asegúrate de tener instalado CircuitPython.
- Ejecuta el archivo main.py en tu Raspberry Pi Pico.
  
Detalles del Código
- generar_aleatorios(): Genera números aleatorios que determinan el tipo de portero.
- AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3): Asigna los LEDs que se van a encender según los valores aleatorios generados.
- gol(): Genera un sonido de victoria.
- no_gol(): Genera un sonido de derrota.
- pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3): Inicializa los botones y LEDs según la configuración del portero.
- El ciclo while True maneja las interacciones del juego.
  
Contribuciones
Este proyecto acepta contribuciones. Si deseas contribuir, asegúrate de seguir las pautas de contribución y enviar commits significativos. Asegúrate de utilizar CircuitPython 9.0.4 o una versión posterior para la revisión.


Autor
Creado por Valeria Montero Barrientos (vamontero@estudiantec.cr) y Sebastián Azofeifa (sazofeifa@estudiantec.cr) 
Link: https://github.com/vamontero/Proyecto.git

