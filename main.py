import whisper
import sys

def transcripter(source, output):
    source = str(source)
    model = whisper.load_model('smal')
    result = model.transcribe(source) 
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <source path>")
        sys.exit(1)

    source = sys.argv[1]
    output = sys.argv[2]

    transcripter(source=source, output=output)