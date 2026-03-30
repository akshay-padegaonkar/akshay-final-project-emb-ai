from EmotionDetection import emotion_detector

texts = [
    "I am glad this happened",
    "I am really mad about this",
    "I feel disgusted just hearing about this",
    "I am so sad about this",
    "I am really afraid that this will happen"
]
#text1 = "I am glad this happened"
#text2 = "I am really mad about this"
#text3 = "I feel disgusted just hearing about this"
#text4 = "I am so sad about this"
#text5 = "I am really afraid that this will happen"

for t in texts:
    results = emotion_detector(t)
    dominant = results.get("dominant_emotion","")
    print(f"{t} -> {dominant}\n")

#result1 = emotion_detector(text1)
#dominant1 = result1.get("dominant_emotion", "")
#print(text1,"->", dominant1)

#result2 = emotion_detector(text2)
#dominant2 = result2.get("dominant_emotion","")
#print(text2, dominant2)

