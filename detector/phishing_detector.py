import re
from urllib.parse import urlparse

def check_phishing(url):
    score = 0
    reasons = []

    # Check for IP address in URL
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 2
        reasons.append("URL contains an IP address")

    # URL length check
    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long")

    # Suspicious keywords
    keywords = ["login", "verify", "secure", "account", "update", "bank"]
    for word in keywords:
        if word in url.lower():
            score += 1
            reasons.append(f"Suspicious keyword found: {word}")

    # Check for excessive dots
    if url.count('.') > 5:
        score += 1
        reasons.append("Too many dots in URL")

    # Check for HTTPS
    if not url.lower().startswith("https"):
        score += 1
        reasons.append("URL does not use HTTPS")

    return score, reasons


def verdict(score):
    if score >= 5:
        return "🚨 HIGH RISK (Likely Phishing)"
    elif score >= 3:
        return "⚠️ SUSPICIOUS"
    else:
        return "✅ LOW RISK"


if __name__ == "__main__":
    url = input("Enter URL to analyze: ").strip()
    score, reasons = check_phishing(url)

    print("\n--- Analysis Result ---")
    print(f"Risk Score: {score}")
    print(f"Verdict: {verdict(score)}")

    if reasons:
        print("\nReasons:")
        for r in reasons:
            print(f"- {r}")
