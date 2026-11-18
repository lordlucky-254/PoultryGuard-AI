# PoultryGuard AI

An explainable poultry-health triage assistant for farmers and animal-health workers.

This repository deliberately separates **triage** from diagnosis. It asks for symptoms, age, flock size, and urgency signals, then returns practical biosecurity steps and a clear recommendation to contact a veterinarian. It does not prescribe drugs or dosages.

## Run

```bash
cd backend
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The web client is `frontend/index.html`. API endpoints are `GET /health` and `POST /api/v1/triage`.

## Next steps

- Add veterinary-reviewed symptom protocols by species and region.
- Add photo triage only after building a field dataset with consent and strong privacy controls.
- Add outbreak clustering from time, location, flock, and mortality signals.
- Validate all recommendations with a qualified veterinary professional before deployment.
