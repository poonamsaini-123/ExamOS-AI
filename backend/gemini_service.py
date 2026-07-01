import subprocess

def analyze_text(text):

    try:
        # ==========================
        # DEBUGGING
        # ==========================
        print("TEXT LENGTH:", len(text))
        print(text[:200])

        # ==========================
        # CHECK IF PDF IS A RESUME
        # ==========================
        text_lower = text.lower()

        resume_keywords = [
            "education",
            "skills",
            "experience",
            "projects",
            "objective",
            "certifications"
        ]

        count = sum(1 for k in resume_keywords if k in text_lower)

        if count < 2:
            return {
                "status": "error",
                "message": "The uploaded PDF does not appear to be a resume."
            }

        # ==========================
        # RUN LEMMA
        # ==========================
        print("Starting Lemma...")

        result = subprocess.run(
            ["lemma", "agent", "run", "examos-agent", text],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

        print("Lemma Finished")

        raw = result.stdout or ""

        # ==========================
        # REMOVE TERMINAL OUTPUT
        # ==========================
        idx = raw.find("Resume Analysis")

        if idx != -1:
            raw = raw[idx:]

        end = raw.find("COMPLETED")

        if end != -1:
            raw = raw[:end]

        raw = raw.strip()

        return {
            "analysis_raw": raw,
            "status": "success"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }