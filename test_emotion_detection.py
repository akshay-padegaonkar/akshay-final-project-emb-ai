from EmotionDetection import emotion_detector

text1 = "I am glad this happened"
text2 = "I am really mad about this"
text3 = "I feel disgusted just hearing about this"
text4 = "I am so sad about this"
text5 = "I am really afraid that this will happen"

result1 = emotion_detector(text1)
dominant1 = result1.get("dominant_emotion", "")
print(dominant1)

result2 = emotion_detector(text2)
dominant2 = result2.get("dominant_emotion","")
print(dominant2)

