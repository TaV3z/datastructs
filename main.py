import sys

try:
    topic = sys.argv
    if __name__ == "__main__":
        with open(f'{topic[1]}.py', "rb") as source_file:
            code = compile(source_file.read(), f'{topic[1]}.py', "exec")
        exec(code)

except:
    print("Some error occurs")

