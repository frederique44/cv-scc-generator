utils/parsers.py
import re
from datetime import datetime

def parse_experience(text):
    """Extrait les expériences pro avec regex avancée"""
    pattern = r"(?i)(\d{2}/\d{4}|[a-zéèê]+ \d{4})[\s\-–]+(?:à|au|\-|–|jusqu'à)?\s*(\d{2}/\d{4}|présent|aujourd'hui)?\s*(.*?)\s*(?:chez|@|à)?\s*(.*?)\s*(?=\d{2}/\d{4}|[A-Z][a-z]+ \d{4}|$)"
    matches = re.finditer(pattern, text, re.DOTALL)
    
    experiences = []
    for match in matches:
        start_date = match.group(1)
        end_date = match.group(2) or "présent"
        position = match.group(3).strip()
        company = match.group(4).strip()
        
        experiences.append({
            "dates": f"{start_date} - {end_date}",
            "position": position,
            "company": company
        })
    
    return experiences
