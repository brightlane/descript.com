import random
from datetime import datetime

from social_poster import generate_post, post_to_x, post_to_linkedin

AFFILIATE = "https://get.descript.com/ejfgu2ujux4j"

# -----------------------------
# DAILY CONTENT TOPICS
# -----------------------------
TOPICS = [
    "AI Video Editing Guide",
    "Descript Review for Creators",
    "Podcast Editing Workflow in 2026",
    "How to Edit Videos 10x Faster",
    "Best AI Tools for Content Creators",
    "Remove Filler Words Automatically",
    "Text-Based Video Editing Explained",
    "YouTube Growth Editing Strategy",
    "Content Repurposing System",
    "Beginner Video Editing Workflow"
]

# -----------------------------
# PLATFORM ADAPTATION
# -----------------------------
def format_for_platform(base_text, platform):
    if platform == "x":
        return base_text[:260] + "\n\n" + AFFILIATE

    if platform == "linkedin":
        return base_text + "\n\n" + AFFILIATE

    return base_text


# -----------------------------
# DAILY GENERATION ENGINE
# -----------------------------
def run_daily_engine():
    today_index = datetime.now().day % len(TOPICS)
    topic = TOPICS[today_index]

    print(f"Generating content for: {topic}")

    # Create base post
    base_post = generate_post(topic)

    # Format per platform
    x_post = format_for_platform(base_post, "x")
    linkedin_post = format_for_platform(base_post, "linkedin")

    print("\n--- X POST ---")
    print(x_post)

    print("\n--- LINKEDIN POST ---")
    print(linkedin_post)

    # -----------------------------
    # OPTIONAL: AUTO POSTING
    # -----------------------------

    # X (Twitter)
    # status, res = post_to_x(
    #     x_post,
    #     "YOUR_X_BEARER_TOKEN"
    # )
    # print("X POST STATUS:", status)

    # LinkedIn
    # status, res = post_to_linkedin(
    #     linkedin_post,
    #     "YOUR_LINKEDIN_TOKEN",
    #     "urn:li:person:YOUR_ID"
    # )
    # print("LINKEDIN STATUS:", status)


# -----------------------------
# RUN DAILY
# -----------------------------
if __name__ == "__main__":
    run_daily_engine()
