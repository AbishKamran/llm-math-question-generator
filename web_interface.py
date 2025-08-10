from flask import Flask, render_template, request, jsonify, send_file
import json
import os
from question_generator import MathQuestionGenerator
from question_analytics import generate_analytics_report
from generate_document import create_word_document

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_questions():
    try:
        data = request.json
        count = data.get('count', 2)
        difficulty = data.get('difficulty', 'adaptive')
        include_latex = data.get('latex', True)
        
        generator = MathQuestionGenerator(
            difficulty_adaptive=(difficulty == 'adaptive'),
            latex_support=include_latex
        )
        
        questions = []
        for i in range(count):
            if i % 2 == 0:
                q = generator.generate_counting_question()
            else:
                q = generator.generate_geometry_question()
            questions.append(q)
        
        # Generate analytics
        analytics = generate_analytics_report(questions)
        
        return jsonify({
            'success': True,
            'questions': questions,
            'analytics': analytics
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/download/<format>')
def download_questions(format):
    try:
        if format == 'docx':
            create_word_document()
            return send_file('Generated_Math_Questions.docx', as_attachment=True)
        elif format == 'txt':
            return send_file('questions_formatted.txt', as_attachment=True)
        else:
            return jsonify({'error': 'Invalid format'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)