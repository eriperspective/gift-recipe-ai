#!/usr/bin/env python3
"""Generate all 4 gift tags for Day 9 challenge"""

import os

# Tag configurations
tags = [
    {
        "filename": "gift-tag-count-harringwell.html",
        "recipient_name": "Count Harringwell",
        "gift_description": "Royal Velvet Tapestry",
        "sender_name": "Baron Covingsmith Festival Court",
        "tag_style": "festive",
        "gradient": "linear-gradient(135deg, #880e4f 0%, #c2185b 100%)",
        "color": "#c2185b",
        "favorite_color": "dark cranberry",
        "language": "Spanish",
        "greeting": "Felices Fiestas",
        "tone": "playful",
        "gift_size": "medium",
        "qr_url": None,
        "icon": "🎭"
    },
    {
        "filename": "gift-tag-duchess-ashlyn-crest.html",
        "recipient_name": "Duchess Ashlyn Crest",
        "gift_description": "Silver Jeweled Chalice",
        "sender_name": "Her Majesty's Winter Festival",
        "tag_style": "elegant",
        "gradient": "linear-gradient(135deg, #1a237e 0%, #0d47a1 100%)",
        "color": "#0d47a1",
        "favorite_color": "navy blue",
        "language": "English",
        "greeting": "Season's Greetings",
        "tone": "formal",
        "gift_size": "medium",
        "qr_url": "https://example.com/thank-you-royal-decree",
        "icon": "👑"
    },
    {
        "filename": "gift-tag-lady-elizabeth-westone.html",
        "recipient_name": "Lady Elizabeth Westone",
        "gift_description": "Artisan Chocolate Collection",
        "sender_name": "Baroness Trystenwald Estate",
        "tag_style": "minimalist",
        "gradient": "linear-gradient(135deg, #5d4037 0%, #795548 100%)",
        "color": "#795548",
        "favorite_color": "medium taupe",
        "language": "Italian",
        "greeting": "Buone Feste",
        "tone": "heartfelt",
        "gift_size": "small",
        "qr_url": "https://example.com/special-message",
        "icon": "🍫"
    },
    {
        "filename": "gift-tag-lord-windmere.html",
        "recipient_name": "Lord Windmere",
        "gift_description": "Noble Manuscripts of Plays",
        "sender_name": "Prince Greyson",
        "tag_style": "playful",
        "gradient": "linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%)",
        "color": "#2e7d32",
        "favorite_color": "dark evergreen",
        "language": "French",
        "greeting": "Joyeuses Fêtes",
        "tone": "humorous",
        "gift_size": "small",
        "qr_url": "https://example.com/noble-message",
        "icon": "📜"
    }
]

# Poems for each tag
poems = {
    "Count Harringwell": """A tapestry of velvet, rich and fine,
To warm thy halls with beauty so divine.
Let festive joy thy noble heart embrace,
As winter's grace adorns this royal place.""",
    
    "Duchess Ashlyn Crest": """A chalice wrought of silver, jewels bright,
To grace thy table in the candlelight.
May this fine vessel hold thy spirits dear,
And bring thee joy throughout the coming year.""",
    
    "Lady Elizabeth Westone": """Sweet chocolates crafted by an artisan's hand,
The finest treats in all the winter land.
Each morsel filled with love and care so true,
A heartfelt gift from me to you.""",
    
    "Lord Windmere": """Manuscripts of plays, both old and new,
For one who loves the stage as scholars do.
May laughter ring from every witty line,
And noble words make merry as we dine."""
}

def generate_tag_html(tag):
    """Generate HTML for a single tag"""
    
    qr_code_html = ""
    if tag["qr_url"]:
        qr_code_html = f'<img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={tag["qr_url"]}" alt="QR Code" class="qr-code">'
    
    poem_html = ""
    if tag["recipient_name"] in poems:
        poem_html = f'<p class="poem">{poems[tag["recipient_name"]]}</p>'
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gift Tag - {tag["recipient_name"]}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Dancing+Script:wght@400;700&family=Merriweather:wght@300;400;700&family=Lora:wght@400;600&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Lora', serif;
            background: #2a2a2a;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }}
        
        .tag-container {{
            perspective: 1000px;
            width: 400px;
            height: 550px;
        }}
        
        .tag {{
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.6s;
            cursor: pointer;
        }}
        
        .tag.flipped {{
            transform: rotateY(180deg);
        }}
        
        .tag-face {{
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
        }}
        
        .tag-front {{
            background: white;
            display: flex;
            flex-direction: column;
        }}
        
        .tag-back {{
            background: white;
            transform: rotateY(180deg);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 40px;
        }}
        
        .ribbon-hole {{
            width: 40px;
            height: 40px;
            background: {tag["gradient"]};
            border-radius: 50%;
            position: absolute;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 10;
            border: 3px solid rgba(255,255,255,0.5);
        }}
        
        .ribbon {{
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 80px;
            background: {tag["gradient"]};
            opacity: 0.3;
            clip-path: polygon(0 0, 100% 0, 100% 70%, 50% 100%, 0 70%);
        }}
        
        .tag-header {{
            background: {tag["gradient"]};
            padding: 50px 30px 30px;
            text-align: center;
            color: white;
            position: relative;
        }}
        
        .tag-content {{
            padding: 30px;
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}
        
        .recipient {{
            font-family: 'Great Vibes', cursive;
            font-size: 42px;
            font-weight: 400;
            margin-bottom: 5px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        .greeting {{
            font-family: 'Dancing Script', cursive;
            font-size: 18px;
            opacity: 0.9;
            font-weight: 600;
        }}
        
        .gift-label {{
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #666;
            font-weight: 600;
        }}
        
        .gift {{
            font-family: 'Merriweather', serif;
            font-size: 20px;
            color: #333;
            font-weight: 700;
        }}
        
        .poem {{
            font-family: 'Dancing Script', cursive;
            font-size: 16px;
            line-height: 1.6;
            color: {tag["color"]};
            font-style: italic;
            padding: 15px;
            background: rgba(0,0,0,0.02);
            border-radius: 10px;
            border-left: 3px solid {tag["color"]};
            white-space: pre-line;
        }}
        
        .sender {{
            font-family: 'Lora', serif;
            font-size: 14px;
            color: #666;
            text-align: right;
            margin-top: auto;
        }}
        
        .sender-label {{
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
            display: block;
            margin-bottom: 5px;
        }}
        
        .sender-name {{
            font-weight: 600;
            color: {tag["color"]};
        }}
        
        .qr-container {{
            border: 5px solid {tag["color"]};
            border-radius: 15px;
            padding: 20px;
            background: white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
        
        .qr-code {{
            width: 200px;
            height: 200px;
            display: block;
        }}
        
        .version {{
            position: absolute;
            bottom: 10px;
            right: 15px;
            font-size: 9px;
            color: rgba(0,0,0,0.3);
            font-family: 'Lora', serif;
        }}
        
        .tag-container:hover .tag-face {{
            box-shadow: 0 20px 60px rgba(0,0,0,0.7), 
                        0 0 40px {tag["color"]}40;
        }}
        
        @media print {{
            body {{
                background: white;
            }}
            .tag-container {{
                page-break-after: always;
            }}
        }}
        
        @media (max-width: 480px) {{
            .tag-container {{
                width: 90vw;
                height: calc(90vw * 1.375);
            }}
        }}
    </style>
</head>
<body>
    <div class="tag-container">
        <div class="tag" onclick="this.classList.toggle('flipped')">
            <!-- Front -->
            <div class="tag-face tag-front">
                <div class="ribbon-hole"></div>
                <div class="ribbon"></div>
                
                <div class="tag-header">
                    <div class="recipient">{tag["recipient_name"]}</div>
                    <div class="greeting">{tag["greeting"]}</div>
                </div>
                
                <div class="tag-content">
                    <div>
                        <div class="gift-label">Gift</div>
                        <div class="gift">{tag["gift_description"]}</div>
                    </div>
                    
                    {poem_html}
                    
                    <div class="sender">
                        <span class="sender-label">From</span>
                        <span class="sender-name">{tag["sender_name"]}</span>
                    </div>
                </div>
                
                <div class="version">v1.0 | Winter Festival 2025</div>
            </div>
            
            <!-- Back -->
            <div class="tag-face tag-back">
                {qr_code_html if qr_code_html else '<p style="color: #999; font-style: italic;">Click to flip back</p>'}
                {f'<div class="qr-container">{qr_code_html}</div>' if qr_code_html else ''}
            </div>
        </div>
    </div>
</body>
</html>'''
    
    return html

# Generate all tags
base_dir = "C:/Users/richp/Documents/goose/day9-gift-tags"
for tag in tags:
    html = generate_tag_html(tag)
    filepath = os.path.join(base_dir, tag["filename"])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated: {tag['filename']}")

print("\n✅ All 4 gift tags generated successfully!")
