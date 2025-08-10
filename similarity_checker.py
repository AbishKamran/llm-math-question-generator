import re
import math
from typing import List, Dict, Tuple
from collections import Counter

class QuestionSimilarityChecker:
    def __init__(self):
        self.stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should'}
        
    def preprocess_text(self, text: str) -> List[str]:
        """Clean and tokenize text"""
        # Remove special characters and convert to lowercase
        text = re.sub(r'[^\w\s]', ' ', text.lower())
        # Split into words and remove stop words
        words = [word for word in text.split() if word not in self.stop_words and len(word) > 2]
        return words
    
    def calculate_cosine_similarity(self, text1: str, text2: str) -> float:
        """Calculate cosine similarity between two texts"""
        words1 = self.preprocess_text(text1)
        words2 = self.preprocess_text(text2)
        
        # Create word frequency vectors
        all_words = set(words1 + words2)
        vector1 = [words1.count(word) for word in all_words]
        vector2 = [words2.count(word) for word in all_words]
        
        # Calculate cosine similarity
        dot_product = sum(a * b for a, b in zip(vector1, vector2))
        magnitude1 = math.sqrt(sum(a * a for a in vector1))
        magnitude2 = math.sqrt(sum(a * a for a in vector2))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        
        return dot_product / (magnitude1 * magnitude2)
    
    def calculate_jaccard_similarity(self, text1: str, text2: str) -> float:
        """Calculate Jaccard similarity between two texts"""
        words1 = set(self.preprocess_text(text1))
        words2 = set(self.preprocess_text(text2))
        
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        return intersection / union if union > 0 else 0.0
    
    def check_structural_similarity(self, q1: Dict, q2: Dict) -> float:
        """Check structural similarity between questions"""
        structure_score = 0.0
        
        # Check if both have tables
        if 'table' in q1 and 'table' in q2:
            structure_score += 0.3
        elif 'table' not in q1 and 'table' not in q2:
            structure_score += 0.1
        
        # Check difficulty levels
        if q1.get('difficulty') == q2.get('difficulty'):
            structure_score += 0.2
        
        # Check topics
        if q1.get('topic') == q2.get('topic'):
            structure_score += 0.3
        
        # Check number of options
        if len(q1.get('options', [])) == len(q2.get('options', [])):
            structure_score += 0.2
        
        return min(1.0, structure_score)
    
    def detect_similarity(self, question1: Dict, question2: Dict) -> Dict:
        """Comprehensive similarity detection"""
        text1 = question1.get('question', '')
        text2 = question2.get('question', '')
        
        cosine_sim = self.calculate_cosine_similarity(text1, text2)
        jaccard_sim = self.calculate_jaccard_similarity(text1, text2)
        structural_sim = self.check_structural_similarity(question1, question2)
        
        # Weighted average
        overall_similarity = (cosine_sim * 0.4 + jaccard_sim * 0.4 + structural_sim * 0.2)
        
        # Determine similarity level
        if overall_similarity >= 0.8:
            level = "Very High"
            risk = "High plagiarism risk"
        elif overall_similarity >= 0.6:
            level = "High"
            risk = "Moderate plagiarism risk"
        elif overall_similarity >= 0.4:
            level = "Moderate"
            risk = "Low plagiarism risk"
        else:
            level = "Low"
            risk = "Minimal risk"
        
        return {
            'cosine_similarity': cosine_sim,
            'jaccard_similarity': jaccard_sim,
            'structural_similarity': structural_sim,
            'overall_similarity': overall_similarity,
            'similarity_level': level,
            'plagiarism_risk': risk,
            'recommendation': self.get_recommendation(overall_similarity)
        }
    
    def get_recommendation(self, similarity: float) -> str:
        """Get recommendation based on similarity score"""
        if similarity >= 0.8:
            return "Questions are too similar. Consider generating new variations."
        elif similarity >= 0.6:
            return "Questions have high similarity. Review and modify if needed."
        elif similarity >= 0.4:
            return "Questions have moderate similarity. This is acceptable for similar topics."
        else:
            return "Questions are sufficiently different."
    
    def batch_similarity_check(self, questions: List[Dict]) -> Dict:
        """Check similarity across multiple questions"""
        results = []
        
        for i in range(len(questions)):
            for j in range(i + 1, len(questions)):
                similarity = self.detect_similarity(questions[i], questions[j])
                similarity['question_pair'] = (i + 1, j + 1)
                results.append(similarity)
        
        # Summary statistics
        if results:
            avg_similarity = sum(r['overall_similarity'] for r in results) / len(results)
            max_similarity = max(r['overall_similarity'] for r in results)
            high_risk_pairs = [r for r in results if r['overall_similarity'] >= 0.6]
        else:
            avg_similarity = 0
            max_similarity = 0
            high_risk_pairs = []
        
        return {
            'individual_comparisons': results,
            'summary': {
                'average_similarity': avg_similarity,
                'maximum_similarity': max_similarity,
                'high_risk_pairs': len(high_risk_pairs),
                'total_comparisons': len(results)
            },
            'recommendations': self.generate_batch_recommendations(results)
        }
    
    def generate_batch_recommendations(self, results: List[Dict]) -> List[str]:
        """Generate recommendations for the entire question set"""
        recommendations = []
        
        high_sim_count = sum(1 for r in results if r['overall_similarity'] >= 0.6)
        
        if high_sim_count > 0:
            recommendations.append(f"Found {high_sim_count} question pairs with high similarity. Consider diversifying question types.")
        
        structural_sim_count = sum(1 for r in results if r['structural_similarity'] >= 0.8)
        if structural_sim_count > len(results) * 0.5:
            recommendations.append("Many questions have similar structure. Add variety in question formats.")
        
        if not recommendations:
            recommendations.append("Question set shows good diversity. No major concerns detected.")
        
        return recommendations