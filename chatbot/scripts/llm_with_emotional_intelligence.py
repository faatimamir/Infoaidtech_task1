from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from hugchat import hugchat
from hugchat.login import Login
app = Flask(__name__, template_folder='templates')
CORS(app)

# Hugchat is logged in with my credentials and saved in /cookies_snapshot files
# sign = Login('**********@gmail.com', '************')
# cookies = sign.login()
# cookie_path_dir = "./cookies_snapshot"
# sign.saveCookiesToDir(cookie_path_dir)
email = 'faatima.mir@gmail.com'
chatbot = hugchat.ChatBot(cookie_path=f"cookies_snapshot/{email}.json")
@app.route('/')
def root():
    return redirect(url_for('user_input'))

@app.route('/favicon.ico')
def favicon():
    return jsonify({'message': 'No favicon available.'}), 404

@app.route('/user-input-form', methods=['GET'])
def user_input():
    return render_template('user_input.html')

@app.route('/analyse-emotion', methods=['POST'])
def analyse_emotion():
    try:
        # Get request parameters
        data = request.form
        
        input_prompt = data.get('input_prompt', '')

        # Validate parameters
        

        # Generate response using hugging face chat-based completions
        response = generate_response(input_prompt)

        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

def generate_response(input_prompt):
    try:
        # Query the chatbot with the input prompt
        query_result = chatbot.query(input_prompt)
        print("Response from chatbot:", query_result)  # Debugging statement
        response_text = query_result.text
        return response_text
    except Exception as e:
        # Handle errors gracefully
        print(f"Error in generate_response: {e}")
        return str(e)

    # Log in to huggingface and grant authorization to huggingchat
    
    # Create a chatbot connection
    # chatbot = hugchat.ChatBot()
    query_result = chatbot.query(prompt)
    print(query_result) # or query_result.text or query_result["text"]


    return query_result.text

if __name__ == '__main__':
    app.run(debug=True, port=8000)
