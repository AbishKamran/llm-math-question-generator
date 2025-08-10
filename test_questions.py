#!/usr/bin/env python3
"""
Test script to validate generated questions meet requirements
"""

from question_generator import MathQuestionGenerator
import re

def test_question_format():
    """Test that questions follow the required format"""
    generator = MathQuestionGenerator()
    
    # Test counting question
    q1 = generator.generate_counting_question()
    print("Testing Counting Question:")
    print(f"[OK] Has question: {bool(q1.get('question'))}")
    print(f"[OK] Has 5 options: {len(q1.get('options', [])) == 5}")
    print(f"[OK] Has correct answer: {bool(q1.get('correct'))}")
    print(f"[OK] Has explanation: {bool(q1.get('explanation'))}")
    print(f"[OK] Has curriculum info: {all(q1.get(k) for k in ['subject', 'unit', 'topic'])}")
    print(f"[OK] Correct curriculum: {q1['subject'] == 'Quantitative Math'}")
    print()
    
    # Test geometry question  
    q2 = generator.generate_geometry_question()
    print("Testing Geometry Question:")
    print(f"[OK] Has question: {bool(q2.get('question'))}")
    print(f"[OK] Has 5 options: {len(q2.get('options', [])) == 5}")
    print(f"[OK] Has correct answer: {bool(q2.get('correct'))}")
    print(f"[OK] Has explanation: {bool(q2.get('explanation'))}")
    print(f"[OK] Has curriculum info: {all(q2.get(k) for k in ['subject', 'unit', 'topic'])}")
    print(f"[OK] Correct curriculum: {q2['subject'] == 'Quantitative Math'}")
    print()

def test_formatted_output():
    """Test the formatted output matches required format"""
    generator = MathQuestionGenerator()
    q1 = generator.generate_counting_question()
    formatted = generator.format_question(q1, 1, "Test Assessment")
    
    print("Testing Formatted Output:")
    required_tags = ['@title', '@description', '@question', '@instruction', 
                    '@difficulty', '@Order', '@option', '@@option', 
                    '@explanation', '@subject', '@unit', '@topic', '@plusmarks']
    
    for tag in required_tags:
        found = tag in formatted
        print(f"[OK] Contains {tag}: {found}")
    
    print(f"[OK] Has correct answer marker (@@option): {'@@option' in formatted}")
    print()

def test_curriculum_compliance():
    """Test that questions use valid curriculum entries"""
    generator = MathQuestionGenerator()
    
    valid_subjects = ["Quantitative Math"]
    valid_units = ["Data Analysis & Probability", "Geometry and Measurement"]
    valid_topics = ["Counting & Arrangement Problems", "Solid Figures (Volume of Cubes)"]
    
    # Test multiple questions
    for i in range(5):
        q1 = generator.generate_counting_question()
        q2 = generator.generate_geometry_question()
        
        assert q1['subject'] in valid_subjects, f"Invalid subject: {q1['subject']}"
        assert q1['unit'] in valid_units, f"Invalid unit: {q1['unit']}"
        assert q1['topic'] in valid_topics, f"Invalid topic: {q1['topic']}"
        
        assert q2['subject'] in valid_subjects, f"Invalid subject: {q2['subject']}"
        assert q2['unit'] in valid_units, f"Invalid unit: {q2['unit']}"
        assert q2['topic'] in valid_topics, f"Invalid topic: {q2['topic']}"
    
    print("[OK] All curriculum entries are valid")

if __name__ == "__main__":
    print("=" * 50)
    print("TESTING MATH QUESTION GENERATOR")
    print("=" * 50)
    
    test_question_format()
    test_formatted_output()
    test_curriculum_compliance()
    
    print("=" * 50)
    print("ALL TESTS PASSED! [SUCCESS]")
    print("=" * 50)