import pytest
from utils.parsers import parse_cv_data, parse_experience, parse_skills

SAMPLE_CV_TEXT = """
John Doe
Ingénieur Systèmes
Compétences Techniques:
Systèmes: • Windows Server • Linux
Outils: • Ansible • Docker
Expérience:
01/2020 - présent • ACME Corp • Ingénieur Senior
- Migration vers le cloud
- Supervision réseau
"""

def test_parse_experience():
    text = """01/2020 - présent • ACME Corp • Ingénieur Senior
- Migration cloud
- Supervision"""
    experiences = parse_experience(text)
    assert len(experiences) == 1
    assert experiences[0]['position'] == "Ingénieur Senior"

def test_parse_skills():
    skills = parse_skills(SAMPLE_CV_TEXT)
    assert "Windows Server" in skills['systems']
    assert "Docker" in skills['tools']

def test_full_parse():
    data = parse_cv_data(SAMPLE_CV_TEXT)
    assert data['job_title'] == "Ingénieur Systèmes"
    assert len(data['experiences']) == 1
