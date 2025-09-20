from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"
def generate_resume(name, email, phone, education, experience, skills, objective):
    prompt = f"""
    You are a professional resume builder AI. Generate a clean, ATS-friendly resume in text format based on the following inputs:

    Name: {name}
    Email: {email}
    Phone: {phone}
    Objective: {objective}
    Education: {education}
    Experience: {experience}
    Skills: {skills}

    Ensure the format includes:
    - Name at top
    - Contact Information
    - Career Objective
    - Education
    - Work Experience
    - Skills
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional resume-building assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0.7
    )

    return response['choices'][0]['message']['content'].strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        education = request.form['education']
        experience = request.form['experience']
        skills = request.form['skills']
        objective = request.form['objective']

        resume = generate_resume(name, email, phone, education, experience, skills, objective)
        return render_template('index.html', resume=resume)

    return render_template('index.html', resume=None)

if __name__ == '__main__':
    app.run(debug=True)