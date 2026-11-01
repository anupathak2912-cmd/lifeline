def evaluate_triage(symptoms: list[str]) -> dict:
    critical_keywords = ["chest pain", "breathing issue", "unconscious", "accident", "heavy bleeding"]
    
    # Check if any critical keyword matches patient symptoms
    is_critical = any(any(crit in s.lower() for crit in critical_keywords) for s in symptoms)
    
    if is_critical:
        return {
            "severity": "CRITICAL",
            "recommended_ambulance": "ALS", # Advanced Life Support
            "priority_score": 10
        }
    else:
        return {
            "severity": "MODERATE/NORMAL",
            "recommended_ambulance": "BLS", # Basic Life Support
            "priority_score": 5
        }