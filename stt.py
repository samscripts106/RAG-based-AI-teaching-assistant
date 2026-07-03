import whisper

model = whisper.load_model("large-v2")

result = model.transcribe(audio = "audios/66_Document Object Model in JavaScript.mp3",
                          language = "hi",
                          task = "translate")

print(result["text"])