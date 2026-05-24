from datetime import datetime

ASTROLOGY_MESSAGES = {
    'Male': 'Your rising sign suggests confidence and leadership.',
    'Female': 'Your rising sign suggests nurturing energy and intuition.',
    'Other': 'You are balanced with a unique blend of sensitivity and willpower.'
}

HEALTH_MESSAGES = [
    'A balanced routine and regular sleep are essential for preserving long-term wellness.',
    'Gentle movement, breath work, and digestive care will keep your energy stable.',
    'Mind-body harmony is especially important for your nervous system and emotional resilience.'
]

CAREER_MESSAGES = [
    'Your chart supports steady advancement through disciplined effort and strategic risk taking.',
    'Career success comes from blending creativity with a practical plan.',
    'Strong communication and teamwork will unlock new opportunities this year.'
]

RELATIONSHIP_MESSAGES = [
    'Partnerships thrive when honest communication is paired with shared purpose.',
    'Marriage energy is supported by emotional maturity and openness to change.',
    'If you are single, you may meet a long-term partner in a setting connected to your work or study.'
]

FAMILY_MESSAGES = [
    'Family bonds are a source of strength; your chart favors caring connections over conflict.',
    'Roots and tradition matter, and you may find comfort in revisiting your family history.',
    'Support from close relatives helps you through major transitions.'
]

FINANCE_MESSAGES = [
    'Your financial picture is stable when you save consistently and avoid impulsive purchases.',
    'Investments in education, property, or long-term savings will pay off with time.',
    'Watch for opportunities to diversify income with creative side projects.'
]

PAST_MESSAGES = [
    'Karmic energy suggests you have carried lessons of service, discipline, and compassionate leadership.',
    'Past challenges helped you become more grounded and purpose-driven.',
    'There is a strong pattern of learning from relationships and turning setbacks into greater clarity.'
]

FUTURE_MESSAGES = [
    'The next 12 to 18 months are favorable for growth, especially in late spring and early autumn.',
    'New beginnings may arrive through travel, learning, or a fresh professional focus.',
    'Keep an open heart; timing will support both inner development and outer achievement.'
]

GROWTH_MESSAGES = [
    'Personal growth is anchored in consistent self-care and setting healthy boundaries.',
    'The more you trust your intuition, the more easily you will navigate uncertainty.',
    'Developing patience now will reward you with better timing and stronger outcomes.'
]

TIMING_MESSAGES = [
    'October through December is especially favorable for career and financial planning.',
    'April and July are strong months for new relationships and long-term commitments.',
    'A quieter winter season is ideal for rest, reflection, and grounding your next chapter.'
]


def calculate_age(dob_str):
    dt = None
    try:
        dt = datetime.fromisoformat(dob_str)
    except Exception:
        pass

    if dt is None:
        for fmt in ('%d/%m/%Y', '%m/%d/%Y'):
            try:
                dt = datetime.strptime(dob_str, fmt)
                break
            except Exception:
                pass

    if dt is None:
        raise ValueError(
            f"Invalid date format for 'dob': {dob_str}. Expected YYYY-MM-DD or DD/MM/YYYY or MM/DD/YYYY"
        )

    today = datetime.now()
    return today.year - dt.year - ((today.month, today.day) < (dt.month, dt.day))


def build_section(title, paragraphs):
    return {
        'title': title,
        'content': '\n'.join(paragraphs)
    }


def generate_report(data):
    required = ['name', 'gender', 'dob', 'tob', 'pob']
    missing = [field for field in required if not data.get(field)]
    if missing:
        raise ValueError(f'Missing required fields: {", ".join(missing)}')

    age = calculate_age(data['dob'])
    name = data['name'].strip()
    gender = data['gender']
    profession = data.get('profession', 'your current profession')
    education = data.get('education', 'your education')
    country = data.get('country', 'Not provided')
    marital_status = data.get('marital_status', 'Not provided')
    pob = data['pob']
    tob = data['tob']

    summary = (
        f"{name} is a {age}-year-old {gender.lower()} born in {pob} at {tob} on {data['dob']}. "
        "This report is generated to give you a broad and detailed look at your health, career, marriage, family, finance, past influences, and future timing."
    )

    sections = [
        build_section('Health', [
            f"Your chart points to a need for regular sleep, calming routines, and careful digestive support.",
            f"Energy levels rise when you combine light movement with time for quiet reflection.",
            f"Avoid burnout by honoring your body’s need for rest during busy seasons."
        ]),
        build_section('Career', [
            f"Your professional path is strengthened by focused planning and decisive action.",
            f"A strong emphasis on responsibility and reliability will earn long-term trust from colleagues and leaders.",
            f"Consider expanding your skills in communication, leadership, or technology to support your next career step."
        ]),
        build_section('Marriage & Relationships', [
            f"Marriage energy in your chart favors steady partnership built on mutual respect and shared goals.",
            f"If you are in a relationship, the year ahead is supportive of deeper emotional connection and partnership growth.",
            f"If you are single, meaningful connections are likely to form through work, study, or travel."
        ]),
        build_section('Family & Home', [
            f"Family support is especially strong, and your home environment acts as an emotional anchor.",
            f"There is an invitation to nurture bonds with siblings, parents, and elders through honest conversation.",
            f"Your chart suggests that grounding your personal life at home will help stabilize broader ambitions."
        ]),
        build_section('Finance & Wealth', [
            f"Your finances benefit from a steady saving plan and avoiding impulsive large purchases.",
            f"Long-term investments in education, property, or business ideas are favored.",
            f"This cycle supports building a secure base and opening small new income streams over time."
        ]),
        build_section('Past Patterns', [
            f"Karmic energy suggests you have carried lessons of responsibility, compassion, and self-mastery.",
            f"Past challenges were preparing you to step into a more grounded and purposeful role.",
            f"Reviewing earlier life lessons will help release tension and reveal the meaning behind your current direction."
        ]),
        build_section('Future Outlook', [
            f"The next year brings opportunities for growth in career, relationships, and personal influence.",
            f"Late spring and autumn are especially favorable for launching new plans, partnerships, or creative projects.",
            f"By staying adaptable and focused, you can make meaningful progress toward your most important goals."
        ]),
        build_section('Personal Growth', [
            f"Your deepest strength is your ability to blend intuition with practical action.",
            f"Growth comes through learning to rest well and speak your truth with confidence.",
            f"Small daily habits in health, learning, and emotional balance will create the biggest long-term shift."
        ]),
        build_section('Timing', [
            f"October through December is a powerful window for financial planning and professional momentum.",
            f"April and July are strong times for new relationships, commitments, or creative launches.",
            f"A quiet winter season is ideal for reflection, rest, and preparing your next chapter."
        ])
    ]

    analysis = [
        f"{ASTROLOGY_MESSAGES.get(gender, ASTROLOGY_MESSAGES['Other'])}",
        f"Age {age} shows a practical mix of ambition and emotional intelligence.",
        f"Your birth details point to strong potential in both private life and public success."
    ]

    recommendations = [
        'Create a daily wellness routine that includes rest, movement, and mindful breathing.',
        'Set clear goals for career growth, then break them into weekly action steps.',
        'Invest time in family conversations and support your closest relationships.',
        'Save consistently and review your spending before committing to new expenses.',
        'Reflect on past lessons and choose one habit to release that no longer serves you.',
        'Plan bigger moves during your strongest timing windows in spring and autumn.'
    ]

    return {
        'name': name,
        'gender': gender,
        'dob': data['dob'],
        'tob': tob,
        'pob': pob,
        'country': country,
        'marital_status': marital_status,
        'profession': profession,
        'education': education,
        'age': age,
        'summary': summary,
        'analysis': analysis,
        'recommendations': recommendations,
        'sections': sections
    }
