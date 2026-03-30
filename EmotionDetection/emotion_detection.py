import json, requests

def emotion_detector(text: str):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    payload = {
        "raw_document": {
            "text": text
        }
    }

#    try:
    response = requests.post(url, headers=headers, json=payload)
#    return response.json()
# Convert to dictionary
    response_dict = json.loads(response.text)

    # Extract emotions
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    result = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": max(emotions, key=emotions.get)
    }
    return result
 #       response.raise_for_status()  # raises error if bad response
 #       return response.json()

 #   except requests.exceptions.RequestException as e:
#        return {"error": str(e)}

#result = emotion_detector("I love this product, it's amazing!")
#print(result)
