from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

def rotate(s, n):
    n = n % len(s)
    return s[-n:] + s[:-n]

def wrap(x):

    if(x > 127):
        x -= 128
    if(x < 0):
        x += 128

    return x

def split(char, x):

    char = ord(char)

    a = char
    b = char

    if char % 2 == 0:
        a = int(char / 2)
        b = int(char / 2)

    else:
        a = int((char + 1 ) / 2)
        b = int((char - 1 ) / 2)

    a += x
    b -= x

    a = wrap(a)
    b = wrap(b)

    a = chr(a)
    b = chr(b)

    return a + b

def encode(message: str) -> str:

	if message == "":
		return ""
	if len(message) == 0:
		return ""

	message = list(message)

	message = rotate(message, datetime.now().minute)

	for i in range(len(message)):
        
		message[i] = split(message[i], i)

	return "".join(message)


https://codeandfeast-blackbox2.chals.io/@app.route("/", methods=["GET", "POST"])
def home():
	output = ""
	user_input = ""

	if request.method == "POST":
		user_input = request.form.get("message", "")
		user_input = user_input[:20]
		output = encode(user_input)

	return render_template_string("""
		<html>
			<body>
				<h2>BlackBoxWarrior 2</h2>
				<p>Note that the output may have some non-printable characters</p> 
				<form method="POST">
					<input type="text" name="message" placeholder="Enter text" />
					<button type="submit">Encode</button>
				</form>
				<p>Input: {{ user_input }}</p>
				<p>Output: {{ output }}</p>
				<br>
				<p>This is not an exploitation challenge, please don't try to break my code</p>
				<p>--Alex</p>

				<!--
And then I look at the pants...
Pants... On fire
Liar!
Liar!
Liar, liar, pants on fire!
I'm living a lie, and a liar's pants must burn!
And so I dash towards the bonfire, and with one fell swoop of my embodied darkness, kick the pants over, sending sparks up into the air and pants-worshipping hippies into a panic, and they all shout
"No, Will! The pants!"
And I say, "I'm sorry, I have to change my life!"
				-->

			</body>
		</html>
	""", output=output, user_input=user_input)

if __name__ == "__main__":
	app.run(debug=False)
