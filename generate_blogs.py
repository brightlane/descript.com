import os
from datetime import datetime, timedelta

AFFILIATE = "https://get.descript.com/ejfgu2ujux4j"

topics = [
    "AI Video Editing Guide",
    "Descript Review",
    "Podcast Editing Workflow",
    "How to Edit Videos Faster",
    "Best AI Tools for Creators",
    "Remove Filler Words Automatically",
    "Text-Based Video Editing Explained",
    "YouTube Editing Workflow",
    "Content Repurposing Strategy",
    "Beginner Video Editing Guide"
]

def generate_blog(day_offset):
    date = (datetime.now() + timedelta(days=day_offset)).strftime("%Y-%m-%d")
    topic = topics[day_offset % len(topics)]

    html = f"""
<html>
<head>
<title>{topic} - Descript Guide</title>
</head>
<body>

<h1>{topic}</h1>

<p>Descript is a real AI editing tool used for video and podcast production.</p>

<a href="{AFFILIATE}">Try Descript Free</a>

<h2>Key Features</h2>
<ul>
<li>Text-based editing</li>
<li>Automatic transcription</li>
<li>Audio cleanup tools</li>
<li>Screen recording</li>
</ul>

<h2>Why It Matters</h2>
<p>It reduces editing time by allowing creators to edit video like a document.</p>

<a href="{AFFILIATE}">Start Now</a>

</body>
</html>
"""

    filename = f"blog-{date}.html"
    with open(filename, "w") as f:
        f.write(html)

for i in range(365):
    generate_blog(i)

print("Done generating 365 blogs")
