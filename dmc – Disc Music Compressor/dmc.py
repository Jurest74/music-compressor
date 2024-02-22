from pydub import AudioSegment
import os
import time
import concurrent.futures
import sys
import time

def is_file_valid(file_path):
    return os.path.isfile(file_path)

def is_folder_valid(folder_path):
    return os.path.isdir(folder_path)

def obtener_tiempo_transcurrido(start_time):
    return time.time() - start_time

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
    start_time = time.time()
    print("Inicia conversion a MP3")
    audio = AudioSegment.from_file(input_cda, format='aiff')
    audio.export(output_format, format='mp3', bitrate=bitrate)
    stop_time = obtener_tiempo_transcurrido(start_time)
    print(f"Finaliza conversion a MP3 - Tiempo: {stop_time:.2f} seg")

    #Impresion tamaño del archivo
    output_size_bytes = os.path.getsize(output_format)
    output_size_megabytes = output_size_bytes / (1024 * 1024)
    print(f"Tamaño del archivo de salida MP3: {output_size_megabytes:.2f} megabytes")

# Convert to WAV
def convert_audio_to_wav(input_cda, output_format, bitrate='192k'):
    start_time = time.time()
    print("Inicia conversion a WAV")
    audio = AudioSegment.from_file(input_cda, format='aiff')
    audio.export(output_format, format='wav', bitrate=bitrate)
    stop_time = obtener_tiempo_transcurrido(start_time)
    print(f"Finaliza conversion a WAV - Tiempo: {stop_time:.2f} seg")

    #Impresion tamaño del archivo
    output_size_bytes = os.path.getsize(output_format)
    output_size_megabytes = output_size_bytes / (1024 * 1024)
    print(f"Tamaño del archivo de salida WAV: {output_size_megabytes:.2f} megabytes")

# Convert to OGG
def convert_audio_to_ogg(input_cda, output_format, bitrate='192k'):
    start_time = time.time()
    print("Inicia conversion a OGG")
    audio = AudioSegment.from_file(input_cda, format='aiff')
    audio.export(output_format, format='ogg', bitrate=bitrate)
    stop_time = obtener_tiempo_transcurrido(start_time)
    print(f"Finaliza conversion a OGG - Tiempo: {stop_time:.2f} seg")
    
    #Impresion tamaño del archivo
    output_size_bytes = os.path.getsize(output_format)
    output_size_megabytes = output_size_bytes / (1024 * 1024)
    print(f"Tamaño del archivo de salida OGG: {output_size_megabytes:.2f} megabytes")

def process_audio_conversion(args):
    #print(args)
    input_file, output_file, conversion_function = args
    conversion_function(input_file, output_file)

def process_audio_conversion_massive(args):
    input_file, output_file, conversion_function = args
    conversion_function(input_file, output_file)

def delete_unnecessary_files(user_input_select_format, output_file_wav, output_file_mp3, output_file_ogg):
    if(user_input_select_format.lower() == 'mp3'):
            os.remove(output_file_wav)
            os.remove(output_file_ogg)
    elif(user_input_select_format.lower() == 'wav'):
            os.remove(output_file_mp3)
            os.remove(output_file_ogg)
    elif(user_input_select_format.lower() == 'ogg'):
            os.remove(output_file_mp3)
            os.remove(output_file_wav)

def process_convert_file_to_all_formats(full_path_input_file, folder_output):
    start_time = time.time()
    output_file_mp3 = os.path.join(os.getcwd(), folder_output.replace('.aif', '.mp3'))
    output_file_wav = os.path.join(os.getcwd(), folder_output.replace('.aif', '.wav'))
    output_file_ogg = os.path.join(os.getcwd(), folder_output.replace('.aif', '.ogg'))

    process_to_all = [(full_path_input_file, output_file_mp3, convert_audio_to_mp3),
                    (full_path_input_file, output_file_wav, convert_audio_to_wav),
                    (full_path_input_file, output_file_ogg, convert_audio_to_ogg)]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Enviar tareas al pool y obtener un objeto Future para cada tarea
        futures = [executor.submit(process_audio_conversion, args) for args in process_to_all]
        # Esperar a que se completen las tareas y obtener los resultados
        resultados_tarea1 = [future.result() for future in concurrent.futures.as_completed(futures)]
        
    stop_time = obtener_tiempo_transcurrido(start_time)

    while True:
        user_input_select_format = input("Por favor, ingresa el formato que deseas: ")
        if user_input_select_format.lower() in ['wav', 'mp3', 'ogg']:
            print(f"\nFormato del archivo convertido: {user_input_select_format.upper()}")
            print(f"Tiempo de conversión: {stop_time:.2f} segundos")
            break  # Salir del bucle si el formato es válido
        else:
            print("Formato no válido. Por favor, ingrese 'wav', 'mp3' o 'ogg'. \n")

    delete_unnecessary_files(user_input_select_format, output_file_wav, output_file_mp3, output_file_ogg)

def process_convert_folder(full_path_input_file, format_output_files, folder_output):
    start_time = time.time()
    proces_to_run = []
    nombres_archivos = obtener_nombres_archivos(full_path_input_file)
    for nombre_archivo in nombres_archivos:
        if(nombre_archivo != '.DS_Store'):
            output_file = os.path.join(os.getcwd(), folder_output, nombre_archivo)
            output_file = output_file.replace('.aif', '.' + format_output_files)
            full_path_input = os.path.join(os.getcwd(), full_path_input_file, nombre_archivo)
            if(format_output_files == 'mp3'):
                proces_to_run.append((full_path_input, output_file, convert_audio_to_mp3))
            elif(format_output_files == 'wav'):
                 proces_to_run.append((full_path_input, output_file, convert_audio_to_wav))
            elif(format_output_files == 'ogg'):
                 proces_to_run.append((full_path_input, output_file, convert_audio_to_ogg))
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Enviar tareas al pool y obtener un objeto Future para cada tarea
        futures = [executor.submit(process_audio_conversion, args) for args in proces_to_run]
        # Esperar a que se completen las tareas y obtener los resultados
        resultados_tarea1 = [future.result() for future in concurrent.futures.as_completed(futures)]
    
    print(f"Formato de la carpeta convertida: {format_output_files.upper()}")
    print(f"Tiempo de conversión: {obtener_tiempo_transcurrido(start_time):.2f} segundos")

def main():
    folder_output = "Output"
    
    if len(sys.argv) < 3 or sys.argv[1] != '-f':
        print("Error: Argumentos insuficientes o incorrectos. \n Use For Files: python3 compressor.py -f [archivo] \n Use For Folders: python3 compressor.py -f [carpeta] [-e=(formato)]")
        sys.exit(1)

    mi_parametro_archivo = sys.argv[2]
    full_path_input_file = os.path.join(os.getcwd(), mi_parametro_archivo)
    full_path_output_file = os.path.join(os.getcwd(), folder_output, mi_parametro_archivo)

    if is_file_valid(full_path_input_file):
        print(f"El archivo {full_path_input_file} es válido.")
        process_convert_file_to_all_formats(full_path_input_file, full_path_output_file)
    elif is_folder_valid(full_path_input_file):
        if len(sys.argv) < 4 or not sys.argv[3].startswith('-e=') or len(sys.argv[3]) <= 3:
            print("Error: Para la conversion de carpetas, se debe especificar el formato de salida con la opción '-e=[Formato]'.")
            sys.exit(1)
        print(f"La carpeta {full_path_input_file} es válida.")
        mi_parametro_e = sys.argv[3]
        format_output_files = mi_parametro_e.split('=')[1]
        if format_output_files.lower() not in ['mp3', 'wav', 'ogg']:
            print("Error: Formato de salida no válido. Utilice mp3, wav u ogg.")
            sys.exit(1)
        print(format_output_files)
        process_convert_folder(full_path_input_file, format_output_files, folder_output)
    else:
        print("Error: Direccion de archivo o carpeta invalida")
        sys.exit(1)

    print("Los Ejecución del programa ha finalizado")

if __name__ == "__main__":
    main()