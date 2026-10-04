import speech_recognition as sr

# Create recognizer object
recognizer = sr.Recognizer()

print("Speech to Text Application")
print("--------------------------")

try:
    # Open microphone
    with sr.Microphone() as source:

        print("Adjusting microphone...")
        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        print("Speak something...")
        
        # Record voice
        audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=10
        )

    print("Processing speech...")

    # Convert speech into text
    text = recognizer.recognize_google(audio)

    print("\nYou said:")
    print(text)

except sr.WaitTimeoutError:
    print("\nNo speech detected.")

except sr.UnknownValueError:
    print("\nSorry, I could not understand your speech.")

except sr.RequestError:
    print("\nSpeech recognition service is unavailable.")

except OSError:
    print("\nMicrophone was not found.")