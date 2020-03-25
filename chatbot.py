import requests
import speech_recognition as sr
import pyttsx3
import time

engine = pyttsx3.init()


def speak(spea):
    engine.say(spea)
    engine.runAndWait()


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "YOUR_API_KEY"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"

    response = requests.get(url, params={"data": text})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


while(1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Say Something")
            #speak("Say Something")
            # r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=1)
        except Exception as e:
            print("Error: ", e)
            audio = ""
    try:
        output = r.recognize_google(audio)
        output = output.lower()
    except Exception as e:
        print("Error: ", e)
        output = ""
    print("Output: ", output)
    if "optimus" in output:
        i = 0
        while(i < 5):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                try:
                    print("How can I help you sir")
                    speak("How can I help you sir")
                    # r.adjust_for_ambient_noise(source)
                    audio = r.listen(source, timeout=1)
                except Exception as e:
                    print("Error: ", e)
                    audio = ""
            try:
                data = r.recognize_google(audio)
                data = data.lower()
            except Exception as e:
                print("Error: ", e)
                data = ""

            if(len(data) > 0):
                if "exit" in data:
                	break
                else: 
		            demo = classify(data)
		            label = demo["class_name"]
		            confidence = demo["confidence"]
		            # CHANGE THIS to do something different with the result
		            output = " Result is " + label + " with " + str(confidence) + "percent confidence"
		            print ("result: '%s' with %d%% confidence" %
		                   (label, confidence))
		            speak(output)
                       
            else:
            	print("No data")
            i = i + 1
            time.sleep(1)
