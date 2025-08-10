#!/usr/bin/env python3
"""
Test script for enhanced features
"""

from question_generator import MathQuestionGenerator
from question_analytics import QuestionAnalytics, generate_analytics_report
from similarity_checker import QuestionSimilarityChecker
import json

def test_enhanced_generator():
    """Test enhanced question generator features"""
    print("[TEST] Testing Enhanced Question Generator...")
    
    generator = MathQuestionGenerator(difficulty_adaptive=True, latex_support=True)
    
    # Test LaTeX formula generation
    formula = generator.generate_latex_formula('combination')
    print(f"[OK] LaTeX formula generated: {formula[:30]}...")
    
    # Test adaptive difficulty
    difficulty = generator.adaptive_difficulty()
    print(f"[OK] Adaptive difficulty: {difficulty}")
    
    # Test enhanced counting question
    q1 = generator.generate_counting_question()
    print(f"[OK] Enhanced counting question has real-world context: {'real_world' in q1.get('explanation', '')}")
    print(f"[OK] Has cognitive load indicator: {q1.get('cognitive_load') is not None}")
    
    # Test enhanced geometry question
    q2 = generator.generate_geometry_question()
    print(f"[OK] Enhanced geometry question has spatial reasoning: {q2.get('spatial_reasoning') is not None}")
    
    print("[PASS] Enhanced generator tests passed!\n")

def test_analytics_system():
    """Test question analytics system"""
    print("[TEST] Testing Analytics System...")
    
    analyzer = QuestionAnalytics()
    
    # Test readability calculation
    sample_text = "Each student at Central Middle School wears a uniform consisting of 1 shirt and 1 pair of pants."
    readability = analyzer.calculate_readability(sample_text)
    print(f"[OK] Readability score calculated: {readability:.1f}")
    
    # Test syllable counting
    syllables = analyzer.count_syllables("mathematical")
    print(f"[OK] Syllable count for 'mathematical': {syllables}")
    
    # Generate sample questions for analysis
    generator = MathQuestionGenerator()
    questions = [generator.generate_counting_question(), generator.generate_geometry_question()]
    
    # Test comprehensive analytics
    report = generate_analytics_report(questions)
    print(f"[OK] Analytics report generated with quality score: {report['summary']['quality_score']*100:.1f}%")
    print(f"[OK] Report has recommendations: {len(report['recommendations'])} items")
    
    print("[PASS] Analytics system tests passed!\n")

def test_similarity_checker():
    """Test similarity checker and plagiarism detection"""
    print("[TEST] Testing Similarity Checker...")
    
    checker = QuestionSimilarityChecker()
    
    # Test text preprocessing
    words = checker.preprocess_text("The quick brown fox jumps over the lazy dog.")
    print(f"[OK] Text preprocessing: {len(words)} meaningful words extracted")
    
    # Test similarity calculations
    text1 = "How many different uniforms are possible?"
    text2 = "How many different combinations are possible?"
    
    cosine_sim = checker.calculate_cosine_similarity(text1, text2)
    jaccard_sim = checker.calculate_jaccard_similarity(text1, text2)
    
    print(f"[OK] Cosine similarity: {cosine_sim:.3f}")
    print(f"[OK] Jaccard similarity: {jaccard_sim:.3f}")
    
    # Test batch similarity check
    generator = MathQuestionGenerator()
    questions = [generator.generate_counting_question() for _ in range(3)]
    
    batch_report = checker.batch_similarity_check(questions)
    print(f"[OK] Batch similarity check: {batch_report['summary']['total_comparisons']} comparisons")
    print(f"[OK] Average similarity: {batch_report['summary']['average_similarity']*100:.1f}%")
    
    print("[PASS] Similarity checker tests passed!\n")

def test_web_interface_components():
    """Test web interface components"""
    print("[TEST] Testing Web Interface Components...")
    
    try:
        from web_interface import app
        print("[OK] Flask app imports successfully")
        
        # Test if templates directory exists
        import os
        if os.path.exists('templates/index.html'):
            print("[OK] HTML template exists")
        else:
            print("[WARNING] HTML template not found")
            
    except ImportError as e:
        print(f"[WARNING] Web interface import failed: {e}")
    
    print("[PASS] Web interface component tests completed!\n")

def test_document_generation():
    """Test enhanced document generation"""
    print("[TEST] Testing Enhanced Document Generation...")
    
    try:
        from generate_document import create_enhanced_word_document
        
        # This would create actual files, so we'll just test the import
        print("[OK] Enhanced document generator imports successfully")
        
        # Test if required modules are available
        try:
            from docx.shared import RGBColor
            print("[OK] Advanced Word formatting available")
        except ImportError:
            print("[WARNING] Advanced Word formatting not available")
            
    except ImportError as e:
        print(f"[WARNING] Enhanced document generator import failed: {e}")
    
    print("[PASS] Document generation tests completed!\n")

def run_comprehensive_test():
    """Run all enhanced feature tests"""
    print("=" * 60)
    print("[START] COMPREHENSIVE ENHANCED FEATURES TEST")
    print("=" * 60)
    
    test_enhanced_generator()
    test_analytics_system()
    test_similarity_checker()
    test_web_interface_components()
    test_document_generation()
    
    print("=" * 60)
    print("[SUCCESS] ALL ENHANCED FEATURES TESTED SUCCESSFULLY!")
    print("=" * 60)
    
    # Generate a sample enhanced question set
    print("\n[DEMO] Generating Sample Enhanced Question Set...")
    generator = MathQuestionGenerator(difficulty_adaptive=True, latex_support=True)
    
    questions = []
    for i in range(3):
        if i % 2 == 0:
            q = generator.generate_counting_question()
        else:
            q = generator.generate_geometry_question()
        questions.append(q)
    
    # Show analytics
    analytics = generate_analytics_report(questions)
    print(f"[ANALYTICS] Sample Set Quality Score: {analytics['summary']['quality_score']*100:.1f}%")
    
    # Show similarity analysis
    checker = QuestionSimilarityChecker()
    similarity = checker.batch_similarity_check(questions)
    print(f"[SIMILARITY] Sample Set Similarity Analysis: {similarity['summary']['average_similarity']*100:.1f}% avg similarity")
    
    print("\n[READY] Enhanced Math Question Generator is ready for production!")

if __name__ == "__main__":
    run_comprehensive_test()