from flask import Flask, render_template , request

app = Flask(__name__)

def generate_square(alphabet, columns, rows):
    characters = list(alphabet.upper())
    square = [[characters[j * rows + i] for i in range(rows)] for j in range(columns)]
    return square


def find_coordinates(char, square):
        for i in range(len(square)):
            for j in range(len(square[0])):
                if square[i][j] == char:
                    return i, j

def encode(alphabet, message , square):
        ciphertext = ""
        for char in message:
            if char.upper() in alphabet:
                row, col = find_coordinates(char.upper(), square)
                ciphertext += str(row + 1) + str(col + 1)
        return ciphertext

def decode(ciphertext, square):
        plaintext = ""
        for i in range(0, len(ciphertext), 2):
            row, col = int(ciphertext[i]) - 1, int(ciphertext[i + 1]) - 1
            plaintext += square[row][col]
        return plaintext




    

@app.route("/", methods=["POST", "GET"])
def process_data():
    result = None

    if request.method == "POST":
        message = request.form["message"]
        operation = request.form["operation"]
        alphabet = request.form["alphabet"]
        rows = int(request.form["rows"])
        columns = int(request.form["columns"])

        square = generate_square(alphabet, columns, rows)

        if operation == "encrypt":
            result = encode(alphabet, message, square)
        elif operation == "decrypt":
            result = decode(message, square)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)