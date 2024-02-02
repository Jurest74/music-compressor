import subprocess
from pydub import AudioSegment
import threading

def extract_audio_to_wav(input_cda, output_wav):
    # Utilizar ffmpeg_command para extraer el audio en formato WAV
    ffmpeg_command = ['ffmpeg', '-i', input_cda, output_wav]
    print(ffmpeg_command)
    subprocess.run(ffmpeg_command)

def extract_audio_to_mp3(input_cda, output_mp3):
    # Utilizar ffmpeg_command para extraer el audio en formato MP3
    ffmpeg_command = ['ffmpeg', '-i', input_cda, output_mp3]
    print(ffmpeg_command)
    subprocess.run(ffmpeg_command)

def extract_audio_to_mp4(input_cda, output_mp4):
    # Utilizar ffmpeg_command para extraer el audio en formato MP4
    ffmpeg_command = ['ffmpeg', '-i', input_cda, output_mp4]
    print(ffmpeg_command)
    subprocess.run(ffmpeg_command)

def main():
    input_cda = './Input/ReminiscenciasCopy.cda'
    output_wav = './Output/ReminiscenciasWav.wav'
    output_mp3 = './Output/ReminiscenciasMP3.mp3'
    output_mp4 = './Output/ReminiscenciasMP4.mp4'

    # Creamos los dos hilos
    hilo_wav = threading.Thread(target=extract_audio_to_wav(input_cda, output_wav))
    hilo_mp3 = threading.Thread(target=extract_audio_to_mp3(input_cda, output_mp3))
    hilo_mp4 = threading.Thread(target=extract_audio_to_mp4(input_cda, output_mp4))

    # Iniciar los hilos
    hilo_wav.start()
    hilo_mp3.start()
    hilo_mp4.start()

    # Esperar a que ambos hilos terminen
    hilo_wav.join()
    hilo_mp3.join()
    hilo_mp4.join()

    print("Los hilos han terminado.")

if __name__ == "__main__":
    main()