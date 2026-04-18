import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    # 1. URL Length
    features.append(len(url))

    # 2. Has IP address
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    features.append(1 if re.search(ip_pattern, url) else 0)

    # 3. Count of dots
    features.append(url.count('.'))

    # 4. Count of hyphens
    features.append(url.count('-'))

    # 5. Count of @
    features.append(url.count('@'))

    # 6. Count of ?
    features.append(url.count('?'))

    # 7. Count of %
    features.append(url.count('%'))

    # 8. Count of =
    features.append(url.count('='))

    # 9. Count of http/https
    features.append(1 if "https" in url else 0)

    # 10. Length of domain
    parsed = urlparse(url)
    features.append(len(parsed.netloc))

    # 👉 Make sure length = same as training features
    # If your model expects 17 features, pad with 0

    while len(features) < 17:
        features.append(0)

    return features