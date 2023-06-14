def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    greeting=func("""Thanks, ms""")
    print(greeting)
greet(shout)
greet(whisper)
