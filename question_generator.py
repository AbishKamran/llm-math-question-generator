import random
import json
import math
from typing import List, Dict, Tuple
from datetime import datetime

class MathQuestionGenerator:
    def __init__(self, difficulty_adaptive=True, latex_support=True):
        self.difficulty_adaptive = difficulty_adaptive
        self.latex_support = latex_support
        self.question_history = []
        self.difficulty_weights = {'easy': 0.4, 'moderate': 0.4, 'hard': 0.2}
        self.curriculum = {
            "Quantitative Math": {
                "Data Analysis & Probability": [
                    "Counting & Arrangement Problems",
                    "Probability (Basic, Compound Events)",
                    "Mean, Median, Mode, & Range"
                ],
                "Geometry and Measurement": [
                    "Area & Volume",
                    "Solid Figures (Volume of Cubes)",
                    "Coordinate Geometry"
                ],
                "Numbers and Operations": [
                    "Fractions, Decimals, & Percents",
                    "Basic Number Theory"
                ]
            }
        }
    
    def generate_latex_formula(self, formula_type: str) -> str:
        """Generate LaTeX formulas for enhanced questions"""
        formulas = {
            'combination': r'C(n,r) = \frac{n!}{r!(n-r)!}',
            'permutation': r'P(n,r) = \frac{n!}{(n-r)!}',
            'volume_sphere': r'V = \frac{4}{3}\pi r^3',
            'volume_cylinder': r'V = \pi r^2 h',
            'area_circle': r'A = \pi r^2'
        }
        return formulas.get(formula_type, '')
    
    def adaptive_difficulty(self) -> str:
        """Dynamically adjust difficulty based on question history"""
        if not self.difficulty_adaptive or len(self.question_history) < 3:
            return random.choices(['easy', 'moderate', 'hard'], 
                                weights=[0.4, 0.4, 0.2])[0]
        
        recent_difficulties = [q.get('difficulty', 'moderate') for q in self.question_history[-3:]]
        if recent_difficulties.count('easy') >= 2:
            return random.choice(['moderate', 'hard'])
        elif recent_difficulties.count('hard') >= 2:
            return random.choice(['easy', 'moderate'])
        return random.choice(['easy', 'moderate', 'hard'])
    
    def generate_counting_question(self) -> Dict:
        """Generate a counting/combination question similar to the uniform question"""
        scenarios = [
            {
                "context": "school cafeteria menu",
                "item1": "sandwich", "item1_options": ["Turkey", "Ham", "Veggie", "Chicken"],
                "item2": "drink", "item2_options": ["Water", "Juice", "Milk"],
                "question": "How many different lunch combinations are possible?",
                "real_world": "This applies to menu planning in restaurants and cafeterias."
            },
            {
                "context": "art class supplies",
                "item1": "paintbrush", "item1_options": ["Small", "Medium", "Large"],
                "item2": "paint color", "item2_options": ["Red", "Blue", "Green", "Yellow", "Purple"],
                "question": "How many different painting setups are possible?",
                "real_world": "Artists use this principle when planning color palettes and tool combinations."
            },
            {
                "context": "computer password creation",
                "item1": "letter", "item1_options": ["A", "B", "C", "D"],
                "item2": "number", "item2_options": ["1", "2", "3"],
                "question": "How many different 2-character passwords (1 letter + 1 number) are possible?",
                "real_world": "This concept is fundamental in cybersecurity and password strength analysis."
            }
        ]
        
        scenario = random.choice(scenarios)
        correct_answer = len(scenario["item1_options"]) * len(scenario["item2_options"])
        
        # Generate wrong answers
        options = [correct_answer]
        while len(options) < 5:
            wrong = random.choice([
                len(scenario["item1_options"]) + len(scenario["item2_options"]),
                len(scenario["item1_options"]),
                len(scenario["item2_options"]),
                correct_answer + random.randint(1, 5),
                correct_answer - random.randint(1, 3) if correct_answer > 3 else correct_answer + 2
            ])
            if wrong > 0 and wrong not in options:
                options.append(wrong)
        
        random.shuffle(options)
        correct_index = options.index(correct_answer)
        
        return {
            "question": f"Each student choosing from the {scenario['context']} selects 1 {scenario['item1']} and 1 {scenario['item2']}. The table shows the options available. {scenario['question']}",
            "table": f"| {scenario['item1'].title()} | {scenario['item2'].title()} |\n|:---:|:---:|\n" + 
                    "\n".join([f"| {opt} | {scenario['item2_options'][i] if i < len(scenario['item2_options']) else ''} |" 
                              for i, opt in enumerate(scenario['item1_options'])]),
            "options": [(chr(65+i), str(opt)) for i, opt in enumerate(options)],
            "correct": chr(65 + correct_index),
            "explanation": f"Using the multiplication principle: {len(scenario['item1_options'])} {scenario['item1']} options × {len(scenario['item2_options'])} {scenario['item2']} options = {correct_answer} total combinations.\n\n**Real-world application:** {scenario['real_world']}\n\n**Formula:** For independent choices, total combinations = n₁ × n₂",
            "latex_formula": self.generate_latex_formula('combination') if self.latex_support else None,
            "subject": "Quantitative Math",
            "unit": "Data Analysis & Probability", 
            "topic": "Counting & Arrangement Problems",
            "difficulty": self.adaptive_difficulty(),
            "cognitive_load": "low" if correct_answer <= 12 else "medium"
        }
    
    def generate_geometry_question(self) -> Dict:
        """Generate a geometry question similar to the ball packing question"""
        scenarios = [
            {
                "shape": "cylinder",
                "radius": 3,
                "arrangement": "4 cylinders in a 2×2 grid",
                "context": "cylindrical cans",
                "real_world": "Used in warehouse storage optimization and shipping container design."
            },
            {
                "shape": "sphere", 
                "radius": 1.5,
                "arrangement": "8 spheres in a 2×2×2 arrangement",
                "context": "spherical ornaments",
                "real_world": "Applied in molecular chemistry and crystal structure analysis."
            },
            {
                "shape": "cube",
                "radius": 2,  # side length
                "arrangement": "6 cubes in a 2×3×1 arrangement",
                "context": "cubic boxes",
                "real_world": "Essential for logistics and 3D printing space optimization."
            }
        ]
        
        scenario = random.choice(scenarios)
        r = scenario["radius"]
        
        if "2×2 grid" in scenario["arrangement"]:
            length = 4 * r
            width = 4 * r  
            height = 2 * r
            correct = f"{int(length)} × {int(width)} × {int(height)}"
        elif "2×2×2" in scenario["arrangement"]:
            length = 4 * r
            width = 4 * r
            height = 6 * r
            correct = f"{int(length)} × {int(width)} × {int(height)}"
        else:  # 2×3×1
            length = 4 * r
            width = 6 * r
            height = 2 * r
            correct = f"{int(length)} × {int(width)} × {int(height)}"
        
        # Generate options
        options = [correct]
        base_dims = [int(length), int(width), int(height)]
        
        while len(options) < 5:
            # Create variations
            variation = [
                f"{base_dims[0]//2} × {base_dims[1]} × {base_dims[2]}",
                f"{base_dims[0]} × {base_dims[1]//2} × {base_dims[2]}",
                f"{base_dims[0]+2} × {base_dims[1]+2} × {base_dims[2]+2}",
                f"{base_dims[0]-1} × {base_dims[1]-1} × {base_dims[2]}"
            ]
            for var in variation:
                if var not in options and len(options) < 5:
                    options.append(var)
        
        random.shuffle(options)
        correct_index = options.index(correct)
        
        return {
            "question": f"A rectangular container holds {scenario['arrangement']} of {scenario['context']}. If each {scenario['shape']} has a radius of {r} centimeters, what are the closest dimensions, in centimeters, of the rectangular container?",
            "options": [(chr(65+i), opt) for i, opt in enumerate(options)],
            "correct": chr(65 + correct_index),
            "explanation": f"Each {scenario['shape']} has diameter {2*r} cm. The arrangement requires {correct} cm dimensions.\n\n**Real-world application:** {scenario['real_world']}\n\n**Volume calculation:** {self.generate_latex_formula('volume_' + scenario['shape']) if scenario['shape'] != 'cube' else 'V = s³'}",
            "latex_formula": self.generate_latex_formula('volume_' + scenario['shape']) if self.latex_support else None,
            "subject": "Quantitative Math",
            "unit": "Geometry and Measurement",
            "topic": "Solid Figures (Volume of Cubes)",
            "difficulty": self.adaptive_difficulty(),
            "spatial_reasoning": "high"
        }
    
    def format_question(self, q_data: Dict, question_num: int, title: str = "Math Assessment") -> str:
        """Format question according to specified output format"""
        if question_num == 1:
            output = f"@title {title}\n@description Assessment of mathematical problem-solving skills\n\n"
        else:
            output = ""
            
        output += f"@question {q_data['question']}\n"
        if 'table' in q_data:
            output += f"\n{q_data['table']}\n\n"
        output += f"@instruction Choose the best answer from the options below.\n"
        output += f"@difficulty {q_data['difficulty']}\n"
        output += f"@Order {question_num}\n"
        
        for letter, option in q_data['options']:
            if letter == q_data['correct']:
                output += f"@@option {option}\n"
            else:
                output += f"@option {option}\n"
        
        output += f"@explanation\n{q_data['explanation']}\n"
        output += f"@subject {q_data['subject']}\n"
        output += f"@unit {q_data['unit']}\n" 
        output += f"@topic {q_data['topic']}\n"
        output += f"@plusmarks 1\n\n"
        
        # Add LaTeX formula if present
        if q_data.get('latex_formula'):
            output += f"@formula ${q_data['latex_formula']}$\n"
        
        return output

def main():
    generator = MathQuestionGenerator()
    
    # Generate questions
    q1 = generator.generate_counting_question()
    q2 = generator.generate_geometry_question()
    
    # Format output
    output = generator.format_question(q1, 1, "Mathematical Reasoning Assessment")
    output += generator.format_question(q2, 2)
    
    return output

if __name__ == "__main__":
    result = main()
    print(result)