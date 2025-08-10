# 🧮 AI-Powered Math Question Generation System

An advanced, AI-driven system that generates high-quality math questions with comprehensive analytics, plagiarism detection, and quality assessment features.

## 🌟 Standout Features

### 🤖 **AI-Powered Question Generation**
- **Adaptive Difficulty**: Dynamically adjusts question difficulty based on generation history
- **LaTeX Formula Support**: Automatically generates mathematical formulas in LaTeX format
- **Real-World Context**: Questions include practical applications and real-world scenarios
- **Cognitive Load Analysis**: Tracks and optimizes cognitive complexity

### 📊 **Advanced Analytics Dashboard**
- **Quality Scoring**: Comprehensive quality assessment (67-85% typical scores)
- **Readability Analysis**: Flesch Reading Ease calculation for accessibility
- **Engagement Metrics**: Measures question engagement factors
- **Difficulty Alignment**: Validates stated vs. actual question complexity

### 🔍 **AI Plagiarism Detection**
- **Similarity Analysis**: Cosine and Jaccard similarity algorithms
- **Structural Comparison**: Analyzes question format and structure
- **Batch Processing**: Checks entire question sets for originality
- **Risk Assessment**: Provides plagiarism risk levels and recommendations

### 🌐 **Interactive Web Interface**
- **Modern UI**: Responsive design with Tailwind CSS
- **Real-time Analytics**: Live quality metrics and similarity scores
- **MathJax Integration**: Beautiful mathematical formula rendering
- **Export Options**: Download as Word documents or formatted text

### 📄 **Enhanced Document Generation**
- **Professional Formatting**: Color-coded answers and quality indicators
- **Analytics Integration**: Embedded quality reports in documents
- **Multiple Formats**: Word documents, formatted text, and JSON reports
- **Visual Elements**: Tables, charts, and structured layouts

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Generate questions with analytics
python generate_document.py

# Run web interface
python web_interface.py

# Test all features
python test_enhanced_features.py
```

## 📁 Project Structure

```
MathQuestionGeneration/
├── 🧠 Core Generation
│   ├── question_generator.py      # Enhanced AI question generator
│   └── generate_document.py       # Advanced document creation
├── 📊 Analytics & Quality
│   ├── question_analytics.py      # Quality assessment system
│   └── similarity_checker.py      # Plagiarism detection
├── 🌐 Web Interface
│   ├── web_interface.py          # Flask web application
│   └── templates/index.html       # Modern web UI
├── 🧪 Testing & Validation
│   ├── test_questions.py         # Basic functionality tests
│   └── test_enhanced_features.py # Comprehensive feature tests
└── 📄 Output Files
    ├── Enhanced_Math_Questions.docx
    ├── analytics_report.json
    └── questions_formatted.txt
```

## 🎯 Generated Question Types

### 1. **Counting & Arrangement Problems**
- School cafeteria menu combinations
- Art class supply arrangements  
- Computer password creation scenarios
- **Real-world applications**: Restaurant planning, cybersecurity

### 2. **Geometry & Measurement Problems**
- 3D container packing optimization
- Sphere and cylinder arrangements
- Cubic box storage solutions
- **Real-world applications**: Warehouse logistics, molecular chemistry

## 📈 Quality Metrics

| Metric | Typical Range | Description |
|--------|---------------|-------------|
| **Quality Score** | 60-85% | Overall question quality assessment |
| **Readability** | 70-90 | Flesch Reading Ease score |
| **Engagement** | 65-80% | Student engagement potential |
| **Similarity** | <30% | Plagiarism risk assessment |

## 🔧 Advanced Configuration

```python
# Adaptive difficulty with LaTeX support
generator = MathQuestionGenerator(
    difficulty_adaptive=True,
    latex_support=True
)

# Generate with analytics
questions = [generator.generate_counting_question() for _ in range(5)]
analytics = generate_analytics_report(questions)
similarity = QuestionSimilarityChecker().batch_similarity_check(questions)
```

## 🎨 Web Interface Features

- **📊 Real-time Analytics**: Live quality scoring and metrics
- **🔍 Similarity Detection**: Instant plagiarism risk assessment  
- **📱 Responsive Design**: Works on desktop, tablet, and mobile
- **⚡ Fast Generation**: Optimized for quick question creation
- **📥 Multiple Exports**: Word, text, and JSON formats

## 🏆 Competitive Advantages

1. **🧠 AI-Powered**: Uses advanced algorithms for quality and originality
2. **📊 Data-Driven**: Comprehensive analytics and reporting
3. **🔍 Plagiarism-Safe**: Built-in similarity detection and prevention
4. **🌐 Modern Interface**: Professional web application
5. **📄 Publication-Ready**: High-quality document generation
6. **🎯 Curriculum-Aligned**: Follows educational standards
7. **⚡ Scalable**: Handles large question sets efficiently

## 📚 Curriculum Coverage

**Subject**: Quantitative Math
- **Data Analysis & Probability** → Counting & Arrangement Problems
- **Geometry and Measurement** → Solid Figures (Volume of Cubes)

## 🔬 Technical Specifications

- **Python 3.11+** with advanced libraries
- **Flask** web framework for modern UI
- **python-docx** for professional document generation
- **MathJax** for LaTeX formula rendering
- **Tailwind CSS** for responsive design
- **Advanced NLP** algorithms for similarity detection

## 📊 Sample Analytics Output

```json
{
  "summary": {
    "quality_score": 0.674,
    "avg_readability": 84.9,
    "avg_engagement": 0.75,
    "total_questions": 4
  },
  "similarity_analysis": {
    "average_similarity": 0.249,
    "high_risk_pairs": 0,
    "recommendations": ["Question set shows good diversity"]
  }
}
```

## 🚀 Future Enhancements

- **Machine Learning**: Adaptive question difficulty based on student performance
- **Multi-Language**: Support for multiple languages and locales
- **Image Generation**: AI-generated diagrams and visual elements
- **Database Integration**: Question bank management and versioning
- **API Endpoints**: RESTful API for integration with LMS systems

---
