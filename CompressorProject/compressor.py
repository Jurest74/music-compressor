import subprocess
from pydub import AudioSegment
import threading
import os
import multiprocessing
import time
import concurrent.futures
import sys


def obtener_nombres_archivos(ruta_carpeta):
    try:
        # Obtener la lista de archivos en la carpeta
        archivos = os.listdir(ruta_carpeta)
        return archivos
    except OSError as e:
        print(f"Error al obtener nombres de archivos en la carpeta {ruta_carpeta}: {e}")
        return []

# Convert to MP3
def convert_audio_to_mp3(input_cda, output_format, bitrate='192k'):
    print("Inicia conversion a MP3")
    audio = AudioSegment.from_file(input_cda, format='aiff')
    time.sleep(3) 
    audio.export(output_format, format='mp3', bitrate=bitrate)
    print("Finaliza conversion a MP3")

    #Impresion tamaño del archivo
    output_size_bytes = os.path.getsize(output_format)
    output_size_megabytes = output_size_bytes / (1024 * 1024)
    print(f"Tamaño del archivo de salida MP3: {output_size_megabytes:.2f} megabytes")

# Convert to WAV
def convert_audio_to_wav(input_cda, output_format, bitrate='192k'):
    print("Inicia conversion a WAV")
    audio = AudioSegment.from_file(input_cda, format='aiff')
    time.sleep(2) 
    audio.export(output_format, format='wav', bitrate=bitrate)
    print("Finaliza conversion a WAV")

    #Impresion tamaño del archivo
    output_size_bytes = os.path.getsize(output_format)
    output_size_megabytes = output_size_bytes / (1024 * 1024)
    print(f"Tamaño del archivo de salida WAV: {output_size_megabytes:.2f} megabytes")

# Convert to OGG
def convert_audio_to_ogg(input_cda, output_format, bitrate='192k'):
    print("Inicia conversion a OGG")
    audio = AudioSegment.from_file(input_cda, format='aiff')
    audio.export(output_format, format='ogg', bitrate=bitrate)
    print("Finaliza conversion a OGG")
    #Impresion tamaño del archivo
    output_size_bytes = os.path.getsize(output_format)
    output_size_megabytes = output_size_bytes / (1024 * 1024)
    print(f"Tamaño del archivo de salida OGG: {output_size_megabytes:.2f} megabytes")

def process_audio_conversion(args):
    input_file, output_file, conversion_function = args
    conversion_function(input_file, output_file)

def main():
    folderInput = "Input"
    folderOutput = "Output"
    fileName = "01 What Makes You Beautiful.aif"

    mi_parametro = sys.argv[2]
    print(mi_parametro)

    full_path = os.path.join(os.getcwd(), folderInput, fileName)
    #print("Ruta completa al archivo:", full_path)

    output_file_mp3 = os.path.join(os.getcwd(), folderOutput, fileName.replace('.aif', '.mp3'))
    output_file_wav = os.path.join(os.getcwd(), folderOutput, fileName.replace('.aif', '.wav'))
    output_file_ogg = os.path.join(os.getcwd(), folderOutput, fileName.replace('.aif', '.ogg'))

    proces_to_mp3 = [(full_path, output_file_mp3, convert_audio_to_mp3),
                      (full_path, output_file_wav, convert_audio_to_wav),
                        (full_path, output_file_ogg, convert_audio_to_ogg)]

    with concurrent.futures.ProcessPoolExecutor() as executor:
    # Enviar tareas al pool y obtener un objeto Future para cada tarea
        futures = [executor.submit(process_audio_conversion, args) for args in proces_to_mp3]

    # Esperar a que se completen las tareas y obtener los resultados
        resultados_tarea1 = [future.result() for future in concurrent.futures.as_completed(futures)]

    # Imprimir los resultados de la tarea1
    #print("Resultados Tarea1:", resultados_tarea1)

    # Imprimir los resultados de la tarea2
    #print("Resultados Tarea2:", resultados_tarea2)

    # Imprimir los resultados de la tarea3
    #print("Resultados Tarea3:", resultados_tarea3)

    #nombres_archivos = obtener_nombres_archivos(full_path)
    #if os.path.isdir(full_path):
    #    for nombre_archivo in nombres_archivos:
    #        if(nombre_archivo != '.DS_Store'):
    #            print(nombre_archivo)
    #            output_file = os.path.join(os.getcwd(), folderOutput, nombre_archivo)
    #            output_file = output_file.replace('.aif', '.mp3')
    #            input_file = os.path.join(os.getcwd(), folderInput, nombre_archivo)
    #            threading.Thread(target=convert_audio_to_mp3(input_file, output_file))
         

    print("Los Ejecución del programa ha finalizado")

if __name__ == "__main__":
    main()