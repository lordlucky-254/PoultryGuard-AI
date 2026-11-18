HIGH_RISK = {"sudden deaths", "bloody droppings", "gasping", "twisted neck", "severe weakness"}


def triage_flock(data: dict) -> dict:
    symptoms = {item.strip().lower() for item in data["symptoms"]}
    emergency = bool(symptoms & HIGH_RISK) or data["deaths_last_24h"] >= max(2, data["flock_size"] // 20)
    if emergency:
        urgency = "urgent"
        message = "Isolate sick birds and contact a veterinarian or animal-health officer today."
    elif len(symptoms) >= 2:
        urgency = "soon"
        message = "Separate affected birds, improve ventilation, and arrange a veterinary assessment."
    else:
        urgency = "monitor"
        message = "Record symptoms twice daily, provide clean water and feed, and monitor the flock closely."
    return {
        "urgency": urgency,
        "possible_pattern": "high-risk outbreak pattern" if emergency else "non-specific respiratory or digestive pattern",
        "guidance": message,
        "biosecurity": ["Limit visitors", "Use dedicated footwear", "Clean equipment between pens"],
        "medication_advice": "No medication or dosage is recommended without veterinary confirmation.",
        "needs_veterinarian": emergency or len(symptoms) >= 2,
        "model": "rules-triage-v0",
    }
