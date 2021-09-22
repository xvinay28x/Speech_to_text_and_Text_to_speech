from pydub import AudioSegment

# files                                                                         
#src = "D:/programming/Python/Machine Learning Projects/project_speech_to_text_or_text_to_speech/abc.mp3"
#dst = "D:/programming/Python/Machine Learning Projects/project_speech_to_text_or_text_to_speech/convert.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3("your_file.mp3")
sound.export("file.wav", format="wav")