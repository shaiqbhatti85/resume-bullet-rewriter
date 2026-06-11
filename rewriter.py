import json
from ollama import chat


TONE_MAP = {
    "Impact-driven (quantified results)": "impact-driven with quantified results and strong metrics",
    "Technical depth": "technical depth, architecture decisions, and engineering specifics",
    "Leadership & collaboration": "leadership, mentorship, and cross-functional collaboration",
    "Innovation & problem-solving": "innovation, creative problem-solving, and initiative",
    "FAANG-optimized": "concise, FAANG-style with clear scope, action, and result",
}


def build_prompt(bullet: str, role: str, tone: str) -> str:
    tone_desc = TONE_MAP.get(tone, tone)
    return f"""You are an expert resume coach specializing in {role} roles at top tech companies.

Rewrite the following resume bullet point into exactly 3 distinct improved versions.

Focus for all versions: {tone_desc}
Original bullet: "{bullet}"

Rules:
- Start each bullet with a strong past-tense action verb (e.g. Architected, Engineered, Reduced, Drove, Led)
- Include specific metrics or outcomes where plausible — invent reasonable ones if none are given
- Keep each bullet under 25 words
- No bullet symbols, hyphens, or numbering — plain text only
- Each version must have a clearly different angle or emphasis from the others
- Avoid generic filler phrases like "responsible for" or "worked on"

Return ONLY a valid JSON object with this exact shape, no markdown fences, no explanation, no preamble:
{{"bullets": ["version 1 text here", "version 2 text here", "version 3 text here"]}}"""


def rewrite_bullet(bullet: str, role: str, tone: str) -> dict:
    try:

        prompt = f"""
        You are an expert resume coach.

        Rewrite this resume bullet into exactly 3 stronger versions.

        Role: {role}
        Focus: {tone}

        Bullet:{bullet}

Rules:
- Start each bullet with a strong action verb
- Keep under 25 words
- Make each version different
- Return ONLY the 3 bullets
- One bullet per line
"""

        response = chat(
            model="qwen2.5:1.5b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        raw = response["message"]["content"]

        bullets = []

        for line in raw.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("*"):
                bullets.append(line.lstrip("* ").strip())

            elif line.startswith("-"):
                bullets.append(line.lstrip("- ").strip())

        if len(bullets) < 3:

            bullets = [
                line.strip()
                for line in raw.splitlines()
                if line.strip()
            ]

        return {
            "success": True,
            "bullets": bullets[:3]
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
