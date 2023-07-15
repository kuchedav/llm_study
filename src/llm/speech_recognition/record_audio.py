import sounddevice as sd
import wavio as wv
from pydub import AudioSegment


def record_audio(file_location, duration=5, freq=16000):
    # Record audio
    print("Recording started...")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    # Save the recorded audio as a .wav file
    wv.write(file_location, recording, freq, sampwidth=2)

    # ensure file is wav (otherwise speech to text complains)
    sound = AudioSegment.from_wav(file_location)
    sound.export(file_location, format="wav")
    print(f"Audio saved as {file_location}.")


if __name__ == "__main__":
    file_location = (
        "/Users/davidkuchelmeister/Documents/projects_coding/llm/src/llm/"
        "speech_recognition/recorded_audio.wav"
    )
    record_audio(file_location=file_location, duration=5, freq=16000)
