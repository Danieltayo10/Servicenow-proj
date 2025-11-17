import json
import uuid
from pathlib import Path

INPUT = Path("data/incidents.json")
OUTPUT = Path("output/training_data.jsonl")


def load_incidents():
    with open(INPUT) as f:
        return json.load(f)


def make_classification_sample(inc):
    return {
        "id": str(uuid.uuid4()),
        "task_type": "incident_classification",
        "input": {
            "short_description": inc["short_description"],
            "description": inc["description"],
        },
        "label": inc["category"]
    }


def make_summary_sample(inc):
    return {
        "id": str(uuid.uuid4()),
        "task_type": "summary",
        "input": inc["description"],
        "output": f"A {inc['category']} issue: {inc['short_description']}."
    }


def make_rewrite_sample(inc):
    return {
        "id": str(uuid.uuid4()),
        "task_type": "professional_rewrite",
        "input": inc["description"],
        "output": (
            f"Professional rewrite: {inc['short_description']} "
            f"(Priority {inc['priority']})."
        )
    }


def save_jsonl(records):
    OUTPUT.parent.mkdir(exist_ok=True)
    with open(OUTPUT, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")


def main():
    incidents = load_incidents()
    dataset = []

    for inc in incidents:
        dataset.append(make_classification_sample(inc))
        dataset.append(make_summary_sample(inc))
        dataset.append(make_rewrite_sample(inc))

    save_jsonl(dataset)
    print(f"✔ Generated {len(dataset)} LLM training samples.")


if __name__ == "__main__":
    main()
