def evaluate_triage(symptoms: str) -> dict:
    critical_keywords = ["chest pain", "breathing issue", "unconscious", "accident", "heavy bleeding"]
    
    # Check if any critical keyword matches patient symptoms
    symptoms_lower = symptoms.lower()
    is_critical = any(crit in symptoms_lower for crit in critical_keywords)
    
    if is_critical:
        return {
            "triage_level": "CRITICAL",
            "ambulance_type": "ALS",  # Advanced Life Support
            "priority_score": 10
        }
    else:
        return {
            "triage_level": "MODERATE/NORMAL",
            "ambulance_type": "BLS",  # Basic Life Support
            "priority_score": 5
        }