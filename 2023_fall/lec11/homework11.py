import speech_recognition as sr

def transcribe_wavefile(filename, language='en-US'):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Initialize a variable to hold the recognized text
    recognized_text = ""

    try:
        # Open the file using speech_recognition's AudioFile
        with sr.AudioFile(filename) as source:
            # Record the audio file into an audio data instance
            audio_data = recognizer.record(source)

            # Recognize the speech in the audio file
            recognized_text = recognizer.recognize_google(audio_data, language=language)
    except sr.UnknownValueError:
        # Handle the case where the recognizer could not understand the audio
        recognized_text = "Speech Recognition could not understand audio"
    except sr.RequestError as e:
        # Handle the case where there were issues with the recognizer's request (e.g., no internet connection)
        recognized_text = f"Could not request results from Speech Recognition service; {e}"
    except Exception as e:
        # Handle any other exceptions
        recognized_text = f"An error occurred: {e}"

    # Return the recognized text
    return recognized_text

