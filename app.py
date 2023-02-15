from flask import Flask, render_template, request, jsonify
import openai
import test

app = Flask(__name__)

# Define the route for the form page
@app.route('/')
def index():
    return render_template('form.html')

# Define the route for processing the form data
@app.route('/generate_npc', methods=['POST'])
def generate_npc():
    
    #prompt = "Emilija is a smart, friendly AI Researcher, who has been working in the Advisory Council on Youth of the Council of Europe for years. You ask her: " + request.form['prompt'] 
    
    prompt = "Generate a reply from an expert in Age of Empires 2, to the following question asked by an Age of Empires 2 player: " + request.form['prompt'] + " Please ensure you are replying to this message as an Age of Empires 2 tutorial bot, and using data related to Age of Empires 2."

    openai.api_key = "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"

    # Check if the user is asking for a name
    if any(keyword in prompt.lower() for keyword in ["what's your name", "what is your name", "your name"]):
        npc_text = "My name is Emilija."
    else:
        # Add Emilija's name to the prompt
        prompt = prompt
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.4,
        )
        npc_text = response.choices[0].text
        # npc_text = npc_text.replace("Emilija", "I:")

    return jsonify({'npc_text': npc_text})




if __name__ == '__main__':
    app.run(host="0.0.0.0",port="6900")
