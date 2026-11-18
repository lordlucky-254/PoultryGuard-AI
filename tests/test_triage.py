from backend.app.service import triage_flock


def test_emergency_triage() -> None:
    body = triage_flock({"age_weeks": 8, "flock_size": 50, "symptoms": ["gasping"], "deaths_last_24h": 0})
    assert body["urgency"] == "urgent"


def test_no_drug_prescription() -> None:
    body = triage_flock({"age_weeks": 8, "flock_size": 50, "symptoms": ["low appetite"], "deaths_last_24h": 0})
    assert "dosage" in body["medication_advice"].lower()
