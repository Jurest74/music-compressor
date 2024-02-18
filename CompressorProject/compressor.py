import subprocess
from pydub import AudioSegment
import threading
import os

def obtener_nombres_archivos(ruta_carpeta):
    try:
        # Obtener la lista de archivos en la carpeta
        archivos = os.listdir(ruta_carpeta)
        return archivos
    except OSError as e:
        print(f"Error al obtener nombres de archivos en la carpeta {ruta_carpeta}: {e}")
        return []

def extract_audio_to_wav(input_cda, output_format, bitrate='192k'):
    print(input_cda, output_format)
    # Utilizar ffmpeg_command para extraer el audio en formato WAV
    #ffmpeg_command = ['ffmpeg', '-i', input_cda, output_wav]
    #print(ffmpeg_command)
    #subprocess.run(ffmpeg_command)
    audio = AudioSegment.from_file(input_cda, format='aiff')

    # Convert to MP3
    audio.export(output_format, format='mp3', bitrate=bitrate)
    audio.export(output_format, format='wav', bitrate=bitrate)
    audio.export(output_format, format='ogg', bitrate=bitrate)


#def extract_audio_to_mp3(input_cda, output_format):
    # Utilizar ffmpeg_command para extraer el audio en formato MP3
#    ffmpeg_command = ['ffmpeg', '-i', input_cda, output_format]
#    print(ffmpeg_command)
#    subprocess.run(ffmpeg_command)

#def extract_audio_to_mp4(input_cda, output_mp4):
#    # Utilizar ffmpeg_command para extraer el audio en formato MP4
#    ffmpeg_command = ['ffmpeg', '-i', input_cda, output_mp4]
#    print(ffmpeg_command)
#    subprocess.run(ffmpeg_command)

def main():
    folderInput = "Input"
    folderOutput = "Output"

    full_path = os.path.join(os.getcwd(), folderInput)
    print("Ruta completa:", full_path)
    nombres_archivos = obtener_nombres_archivos(full_path)
    if os.path.isdir(full_path):
        for nombre_archivo in nombres_archivos:
            if(nombre_archivo != '.DS_Store'):
                print(nombre_archivo)
                output_file = os.path.join(os.getcwd(), folderOutput, nombre_archivo)
                output_file = output_file.replace('.aif', '.mp3')
                input_file = os.path.join(os.getcwd(), folderInput, nombre_archivo)
                threading.Thread(target=extract_audio_to_wav(input_file, output_file))
         

        

    # Creamos los dos hilos
    #hilo_wav = threading.Thread(target=extract_audio_to_wav(full_path, output_format))
    #hilo_mp3 = threading.Thread(target=extract_audio_to_mp3(input_cda, output_format))
    #hilo_mp4 = threading.Thread(target=extract_audio_to_mp4(input_cda, output_mp4))

    # Iniciar los hilos
    #hilo_wav.start()
    #hilo_mp3.start()
    #hilo_mp4.start()

    # Esperar a que ambos hilos terminen
    #hilo_wav.join()
    #hilo_mp3.join()
    #hilo_mp4.join()

    print("Los hilos han terminado.")

if __name__ == "__main__":
    main()