import whisper

def transcripter(source):
    source = str(source)
    model = whisper.load_model('medium')
    result = model.transcribe(source) 
    

    