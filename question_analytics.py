import json
import re
from typing import Dict, List
from datetime import datetime
import statistics

class QuestionAnalytics:
    def __init__(self):
        self.metrics = {
            'readability_score': 0,
            'complexity_level': 'medium',
            'cognitive_load': 'balanced',
            'engagement_factors': []
        }
    
    def calculate_readability(self, question_text: str) -> float:
        """Calculate Flesch Reading Ease score"""
        sentences = len(re.split(r'[.!?]+', question_text))
        words = len(question_text.split())
        syllables = sum([self.count_syllables(word) for word in question_text.split()])
        
        if sentences == 0 or words == 0:
            return 50.0
            
        score = 206.835 - (1.015 * words/sentences) - (84.6 * syllables/words)
        return max(0, min(100, score))
    
    def count_syllables(self, word: str) -> int:
        """Estimate syllable count"""
        word = word.lower().strip('.,!?;')
        vowels = 'aeiouy'
        syllable_count = 0
        prev_was_vowel = False
        
        for char in word:
            if char in vowels:
                if not prev_was_vowel:
                    syllable_count += 1
                prev_was_vowel = True
            else:
                prev_was_vowel = False
        
        if word.endswith('e'):
            syllable_count -= 1
        
        return max(1, syllable_count)
    
    def analyze_question_quality(self, question_data: Dict) -> Dict:
        """Comprehensive question quality analysis"""
        analysis = {
            'readability_score': self.calculate_readability(question_data['question']),
            'option_balance': self.analyze_option_distribution(question_data['options']),
            'difficulty_alignment': self.check_difficulty_alignment(question_data),
            'engagement_score': self.calculate_engagement_score(question_data),
            'timestamp': datetime.now().isoformat()
        }
        
        return analysis
    
    def analyze_option_distribution(self, options: List) -> Dict:
        """Analyze if answer options are well-distributed"""
        if not options:
            return {'balanced': False, 'score': 0}
        
        # Extract numeric values where possible
        numeric_options = []
        for _, option in options:
            try:
                # Handle dimension formats like "6 × 6 × 9"
                if '×' in option:
                    nums = [float(x.strip()) for x in option.split('×')]
                    numeric_options.append(sum(nums))  # Use sum as proxy
                else:
                    numeric_options.append(float(option))
            except:
                continue
        
        if len(numeric_options) < 3:
            return {'balanced': True, 'score': 0.8}  # Non-numeric options assumed balanced
        
        # Check if options are reasonably spread
        std_dev = statistics.stdev(numeric_options)
        mean_val = statistics.mean(numeric_options)
        coefficient_variation = std_dev / mean_val if mean_val != 0 else 0
        
        balanced = 0.1 <= coefficient_variation <= 0.5
        score = min(1.0, coefficient_variation * 2) if balanced else 0.3
        
        return {'balanced': balanced, 'score': score, 'cv': coefficient_variation}
    
    def check_difficulty_alignment(self, question_data: Dict) -> Dict:
        """Check if question complexity matches stated difficulty"""
        question_text = question_data['question']
        stated_difficulty = question_data.get('difficulty', 'moderate')
        
        complexity_indicators = {
            'easy': ['select', 'choose', 'how many', 'total'],
            'moderate': ['calculate', 'determine', 'closest', 'arrangement'],
            'hard': ['optimize', 'derive', 'prove', 'analyze']
        }
        
        scores = {}
        for level, indicators in complexity_indicators.items():
            score = sum(1 for indicator in indicators if indicator.lower() in question_text.lower())
            scores[level] = score
        
        predicted_difficulty = max(scores, key=scores.get)
        alignment = predicted_difficulty == stated_difficulty
        
        return {
            'aligned': alignment,
            'predicted': predicted_difficulty,
            'stated': stated_difficulty,
            'confidence': max(scores.values()) / len(complexity_indicators[predicted_difficulty])
        }
    
    def calculate_engagement_score(self, question_data: Dict) -> float:
        """Calculate how engaging the question is"""
        engagement_factors = []
        question_text = question_data['question']
        
        # Real-world context
        if any(word in question_text.lower() for word in ['student', 'school', 'art', 'cafeteria']):
            engagement_factors.append('real_world_context')
        
        # Visual elements
        if 'table' in question_data:
            engagement_factors.append('visual_table')
        
        # Mathematical formulas
        if question_data.get('latex_formula'):
            engagement_factors.append('mathematical_formula')
        
        # Practical application
        if 'real_world' in question_data.get('explanation', ''):
            engagement_factors.append('practical_application')
        
        base_score = 0.5
        bonus = len(engagement_factors) * 0.15
        return min(1.0, base_score + bonus)

def generate_analytics_report(questions: List[Dict]) -> Dict:
    """Generate comprehensive analytics report"""
    analyzer = QuestionAnalytics()
    
    analyses = [analyzer.analyze_question_quality(q) for q in questions]
    
    report = {
        'summary': {
            'total_questions': len(questions),
            'avg_readability': statistics.mean([a['readability_score'] for a in analyses]),
            'avg_engagement': statistics.mean([a['engagement_score'] for a in analyses]),
            'difficulty_distribution': {},
            'quality_score': 0
        },
        'individual_analyses': analyses,
        'recommendations': [],
        'generated_at': datetime.now().isoformat()
    }
    
    # Calculate difficulty distribution
    difficulties = [q.get('difficulty', 'moderate') for q in questions]
    for diff in set(difficulties):
        report['summary']['difficulty_distribution'][diff] = difficulties.count(diff)
    
    # Overall quality score
    quality_factors = [
        statistics.mean([a['readability_score'] for a in analyses]) / 100,
        statistics.mean([a['engagement_score'] for a in analyses]),
        statistics.mean([a['option_balance']['score'] for a in analyses])
    ]
    report['summary']['quality_score'] = statistics.mean(quality_factors)
    
    # Generate recommendations
    if report['summary']['avg_readability'] < 60:
        report['recommendations'].append("Consider simplifying question language for better readability")
    
    if report['summary']['avg_engagement'] < 0.7:
        report['recommendations'].append("Add more real-world contexts and visual elements")
    
    return report