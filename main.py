import whisper
import sys
import platform

def transcripter(source):
    source = str(source)
    model = whisper.load_model('small')
    result = model.transcribe(source) 
    text = result['text']
    

    so = platform.system()
    if so == 'Windows':
        name = source.split('\\')[-1].split('.')[0]
    else:
        name = source.split('/')[-1].split('.')[0]
   
    
    with open(name + '.txt', 'a') as file:
        file.write(text)    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <source path>")
        sys.exit(1)
    
    source = sys.argv[1]


    transcripter(source=source)