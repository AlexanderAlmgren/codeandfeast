from flask import Flask, request, render_template_string

app = Flask(__name__)

def encode(message: str) -> str:

	if message == "":
		return ""

	if len(message) == 0:
		return ""

	message = list(message)

	#flip = 1

	for i in range(len(message)):
		#ascii_val = ord(message[i]) + (i * flip)
		#flip *= -1
		ascii_val = ord(message[i]) + i
		if ascii_val > 127:
			ascii_val -= 127

		message[i] = chr(ascii_val)

	return "".join(message)

@app.route("/", methods=["GET", "POST"])
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
				<h2>BlackBoxWarrior</h2>
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
Growing up, how was your relationship with the fundamentals of conscious existence? Did you have xenon orchid sinews spilling down the outer center of your blooming Escher/Mandelbrot head? And how about claustrophilic tendrils clapping caskets closed on seven-knuckled thumbs, did you get along well with the Gideon Bugler pineal glands, your projector eyes casting sci-fi's on your STR'd strands? Tell me about your nerve to steal nerves of steel from under Bacchus' bloody nose. Did Namibian Himbas tie-dye you, your ears pierced with a Phineas Gage flagpole, did you die before your day?
				-->

			</body>
		</html>
	""", output=output, user_input=user_input)  # <-- FIX HERE

if __name__ == "__main__":
	app.run(debug=False)
