import requests
from datetime import datetime

AFFILIATE = "https://get.descript.com/ejfgu2ujux4j"

# -----------------------------
# SOCIAL POST GENERATOR
# -----------------------------
def generate_post(topic):
    return f"""
{topic}

Editing videos with AI is changing how creators work.

Tools like Descript let you:
- Edit video by editing text
- Remove filler words automatically
- Improve audio quality instantly

Start here:
{AFFILIATE}
"""

# -----------------------------
# POST TO X (TWITTER)
# -----------------------------
def post_to_x(text, bearer_token):
    url = "https://api.twitter.com/2/tweets"

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    data = {
        "text": text
    }

    response = requests.post(url, json=data, headers=headers)
    return response.status_code, response.text


# -----------------------------
# POST TO LINKEDIN
# -----------------------------
def post_to_linkedin(text, access_token, author_urn):
    url = "https://api.linkedin.com/v2/ugcPosts"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.status_code, response.text


# -----------------------------
# MAIN RUNNER
# -----------------------------
if __name__ == "__main__":

    topics = [
        "AI Video Editing Tip",
        "Descript Workflow Hack",
        "Podcast Editing Shortcut",
        "How Creators Save Time",
        "Remove Filler Words Fast"
    ]

    today_topic = topics[datetime.now().day % len(topics)]
    post_text = generate_post(today_topic)

    print("Generated Post:")
    print(post_text)

    # -------------------------
    # OPTIONAL: ENABLE POSTING
    # -------------------------

    # X (Twitter)
    # status, res = post_to_x(post_text, "YOUR_BEARER_TOKEN")
    # print(status, res)

    # LinkedIn
    # status, res = post_to_linkedin(
    #     post_text,
    #     "YOUR_ACCESS_TOKEN",
    #     "urn:li:person:YOUR_ID"
    # )
    # print(status, res)
