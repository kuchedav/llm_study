import speech_recognition as sr
from record_audio import record_audio


# a function to recognize speech in the audio file
# so that we don't repeat ourselves in in other functions
def transcribe_audio(path):
    # create a speech recognition object
    r = sr.Recognizer()

    # use the audio file as the audio source
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        # try converting it to text
        text = r.recognize_google(audio_listened)
    return text


if __name__ == "__main__":
    file_location = (
        "/Users/davidkuchelmeister/Documents/projects_coding/llm/src/llm/"
        "speech_recognition/recorded_audio_2.wav"
    )

    # record audio
    record_audio(file_location=file_location, duration=5, freq=16000)

    print(transcribe_audio(file_location))
