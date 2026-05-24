from datetime import datetime

ASTROLOGY_MESSAGES = {
    'Male': 'Your rising sign suggests confidence and leadership.',
    'Female': 'Your rising sign suggests nurturing energy and intuition.',
    'Other': 'You are balanced with a unique blend of sensitivity and willpower.'
}

def calculate_age(dob_str):
    # Accept multiple common date formats: ISO (YYYY-MM-DD), DD/MM/YYYY, MM/DD/YYYY
    dt = None
    errors = []
    try:
        dt = datetime.fromisoformat(dob_str)
    except Exception as e:
        errors.append(str(e))
    if dt is None:
        for fmt in ('%d/%m/%Y', '%m/%d/%Y'):
            try:
                dt = datetime.strptime(dob_str, fmt)
                break
            except Exception as e:
                errors.append(str(e))
    if dt is None:
        raise ValueError(f"Invalid date format for 'dob': {dob_str}. Expected YYYY-MM-DD or DD/MM/YYYY or MM/DD/YYYY")
    dob = dt
    today = datetime.now()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


def generate_report(data):
    required = ['name', 'gender', 'dob', 'tob', 'pob']
    missing = [field for field in required if not data.get(field)]
    if missing:
        raise ValueError(f'Missing required fields: {", ".join(missing)}')

    age = calculate_age(data['dob'])
    gender = data['gender']
    name = data['name'].strip()
    profession = data.get('profession', 'your current profession')
    education = data.get('education', 'your education background')

    message = ASTROLOGY_MESSAGES.get(gender, ASTROLOGY_MESSAGES['Other'])
    summary = (
        f"{name} is a {age}-year-old {gender.lower()} born in {data['pob']} "
        f"at {data['tob']} on {data['dob']}. {message}"
    )

    report = {
        'name': name,
        'gender': gender,
        'dob': data['dob'],
        'tob': data['tob'],
        'pob': data['pob'],
        'country': data.get('country', 'Not provided'),
        'marital_status': data.get('marital_status', 'Not provided'),
        'profession': profession,
        'education': education,
        'age': age,
        'summary': summary,
        'analysis': [
            f"Your birth chart shows strong focus and ambition in {profession}.",
            "This year brings steady progress and a chance to deepen your personal relationships.",
            "Be mindful of balance between work and self-care, especially around major life decisions."
        ],
        'recommendations': [
            "Take time each day for quiet reflection.",
            "Explore creative self-expression to strengthen your confidence.",
            "Share your goals with close friends or family for support."
        ]
    }

    return report
